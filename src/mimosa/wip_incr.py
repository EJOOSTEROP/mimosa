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
api_headers = {"x-key": "ENV_GIE_XKEY"}
api_query = "date=2023-08-03"  # TODO: make this configurable

""" Notes regarding GIE REST API response:

- encapsulated into a header
- the actual data is captured in a 'data' attribute
- the returned JSON has gas_day as a field in the header. This seems to represent the lates date for which data is available. dlt keeps the name as 'gas_day'.
- the returned JSON has gasDayStart as the field (dlt translates this into gas_day)
"""
timing_key = "gasDayStart"
primary_key = ("gasDayStart", "code")


# TODO: Not clear if merge works ("merge" vs. "append"). Hard to test using the real API.
@dlt.resource(primary_key=primary_key, table_name="storage", write_disposition="merge")
def get_storage_data(
    created_at=dlt.sources.incremental(timing_key, initial_value="2023-07-10"),
    url=api_url,
    headers=api_headers,
    query=api_query,
):
    """Gets storage data from a REST API.

    Returns: Yields the JSON response.
    """
    url = url + "?" + query
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

        # get next page
        if "next" not in response.links:
            break
        url = response.links["next"]["url"]


pipeline = dlt.pipeline(
    pipeline_name="gas_storage_incremental_new",
    destination="duckdb",
    dataset_name="stage_gas",
    export_schema_path="schemas/export",
    import_schema_path="schemas/import",
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
