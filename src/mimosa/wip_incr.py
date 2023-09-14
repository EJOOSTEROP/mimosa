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


@dlt.resource(table_name="storage", write_disposition="append")
def get_storage_data(
    created_at=dlt.sources.incremental("gas_day", initial_value="2023-09-10")
):
    """Gets storage data from GEI API.

    Returns: Yields the JSON response.
    """
    url = "https://agsi.gie.eu/api"
    headers = {"x-key": "ENV_GIE_XKEY"}

    while True:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        yield [response.json()]

        # stop requesting pages if the last element was already older than initial value
        # note: incremental will skip those items anyway, we just do not want to use the api limits
        if created_at.start_out_of_range:
            break

        # get next page
        if "next" not in response.links:
            break
        url = response.links["next"]["url"]


pipeline = dlt.pipeline(
    pipeline_name="gas_storage_incremental",
    destination="duckdb",
    dataset_name="stage_gas",
)
# the response contains a list of issues
load_info = pipeline.run(get_storage_data)
row_counts = pipeline.last_trace.last_normalize_info
logger.debug(row_counts)
logger.debug(load_info)

# TODO: write_disposition='merge' is what we want to do here. https://dlthub.com/docs/getting-started
# TODO: Problem compared to example is that my API does not result in a list of items (more a singe dict). Hence I do the data.append. But I am not sure how to translate this into the yield function.
