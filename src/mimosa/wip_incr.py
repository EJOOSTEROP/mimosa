"""Sample dlt pipeline.

Loads data from European Gas data REST API.

Loads data incrementally into DuckDB.
"""
import os

import dlt
from dlt.sources.helpers import requests
from dotenv import find_dotenv, load_dotenv
from loguru import logger

_ = load_dotenv(find_dotenv())

ENV_GIE_XKEY = os.getenv("ENV_GIE_XKEY")
api_url = "https://agsi.gie.eu/api"
api_headers = {"x-key": ENV_GIE_XKEY}
api_query = "date=2023-08-02"  # TODO: make this configurable

""" Notes regarding GIE REST API response:

- encapsulated into a header
- the actual data is captured in a 'data' attribute
- the returned JSON has gas_day as a field in the header. This seems to represent the lates date for which data is available. dlt keeps the name as 'gas_day'.
- the returned JSON has gasDayStart as the field (dlt translates this into gas_day)
"""
timing_key = "gasDayStart"
primary_key = ("gasDayStart", "code")


@dlt.source
def gei_gas_storage_source():
    """Decorates a function to be a source for GEI gas storage data.

    Returns:
        The storage data obtained from the GEI gas storage API.

    Example usage:
        storage_data = gei_gas_storage_source()

    # TODO: This has no functionality; also, it cannot be used in a pipeline in its current state.
    """
    return get_storage_data(
        url=api_url,
        headers=api_headers,
        query=api_query,
    )


@dlt.resource(primary_key=primary_key, table_name="storage", write_disposition="merge")
def get_storage_data(
    created_at=dlt.sources.incremental(timing_key, initial_value="2023-07-10"),
    url=api_url,
    headers=api_headers,
    query=api_query,
):
    """Gets storage data from a REST API.

    It is assumed that the API responsed contains a "data" field. The data field is a list of dictionaries.

    Returns: Yields the data field of the JSON response.
    """
    url = f"{url}?{query}"
    logger.debug(url)

    # TODO: the pagination is not working
    while True:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        logger.debug(response)
        yield response.json().get("data")

        # stop requesting pages if the last element was already older than initial value
        # note: incremental will skip those items anyway, we just do not want to use the api limits
        # TODO: out of range does not work
        if created_at.start_out_of_range:
            break

        # get next page. TODO: Review the GIE API spec to confirm whether this is supported.
        if "next" not in response.links:
            break
        url = response.links["next"]["url"]


pipeline = dlt.pipeline(
    pipeline_name="gas_storage",
    destination="duckdb",
    dataset_name="stage_gas",
)

# Run pipeline
load_info = pipeline.run(get_storage_data)
row_counts = pipeline.last_trace.last_normalize_info

# Load lineage and run related info into destination
pipeline.run([load_info], table_name="_load_info")
pipeline.run([pipeline.last_trace], table_name="_trace")

# Log outcome
logger.debug(row_counts)
logger.debug(load_info)

# ##############################################################################
# Starting transformation
# TODO: setup properly: https://dlthub.com/docs/dlt-ecosystem/transformations/dbt
""" pipeline = dlt.pipeline(
    pipeline_name='gas_storage', # TODO: do we really want to reuse the same name
    destination='duckdb',
    dataset_name='gas_dbt' # TODO: need to setup source.yml referring to stage_gas schema
) """

pipeline = dlt.pipeline(
    pipeline_name="gas_storage",  # Changing pipeline name causes errors. Maybe try with source.yml.
    destination="duckdb",
    dataset_name="gas",  # TODO: Not certain how this is reflected in the results. A gas schema is created. But the target table seems to be loaded into both targets.
)

venv = dlt.dbt.get_venv(pipeline)

# get runner, optionally pass the venv
dbt = dlt.dbt.package(pipeline, "/workspaces/mimosa/etc/dbt/gie", venv=venv)

models = dbt.run_all()

# on success print outcome
for m in models:
    logger.info(
        f"Model {m.model_name} materialized "
        f"in {m.time} "
        f"with status {m.status} "
        f"and message {m.message}."
    )

# TODO: somehow only the last loaded date is captured by dbt. Pre-existing data in the target is deleted. Prior data in the source tables is not captured.
# SOLVED: when using source.yml all data is loaded.
# TODO: select * from information_schema.schemata
# TODO: select * from information_schema.tables
