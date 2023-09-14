"""Sample dlt pipeline."""
import os

import dlt
from dlt.sources.helpers import requests
from dotenv import find_dotenv, load_dotenv
from loguru import logger

_ = load_dotenv(find_dotenv())

ENV_GIE_XKEY = os.getenv("ENV_GIE_XKEY")

# Create a dlt pipeline that will load
# GIE gas storage data to the DuckDB destination
pipeline = dlt.pipeline(
    pipeline_name="gas_storage", destination="duckdb", dataset_name="stage_gas"
)
# Grab storage data from GEI API
data = []
headers = {"x-key": "ENV_GIE_XKEY"}
response = requests.get("https://agsi.gie.eu/api", headers=headers)
response.raise_for_status()
data.append(response.json())
# Extract, normalize, and load the data
info = pipeline.run(data, table_name="storage")
logger.info(info)

# TODO: 1) does it append or overwrite the DuckDB 2) What does the table even look like? I doubt normalization has taken place. BUT IT DOES.
# TODO: Somehow this is not working anymore.
