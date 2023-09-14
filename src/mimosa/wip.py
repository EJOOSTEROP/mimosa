"""Sample dlt pipeline."""
import os

import dlt
from dlt.sources.helpers import requests
from dotenv import find_dotenv, load_dotenv
from loguru import logger

_ = load_dotenv(find_dotenv())

ENV_GIE_XKEY = os.getenv("ENV_GIE_XKEY")

# url to request GIE storage data
url = "https://agsi.gie.eu/api"
headers = {"x-key": "ENV_GIE_XKEY"}

# make the request and check if succeeded
response = requests.get(url, headers=headers)
response.raise_for_status()

data = []
data.append(response.json())

pipeline = dlt.pipeline(
    pipeline_name="gas_storage",
    destination="duckdb",
    dataset_name="stage_gas",
)
# the response contains a list of issues
load_info = pipeline.run(data, table_name="storage", write_disposition="append")
logger.debug(load_info)

# TODO: write_disposition='merge' is what we want to do here. https://dlthub.com/docs/getting-started
