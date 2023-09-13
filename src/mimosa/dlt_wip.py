"""Sample dlt pipeline."""
import os

import dlt
from dlt.sources.helpers import requests
from dotenv import find_dotenv, load_dotenv
from loguru import logger

_ = load_dotenv(find_dotenv())

ENV_GIE_XKEY = os.getenv("ENV_GIE_XKEY")

# Create a dlt pipeline that will load
# chess player data to the DuckDB destination
pipeline = dlt.pipeline(
    pipeline_name="chess_pipeline", destination="duckdb", dataset_name="player_data"
)
# Grab some player data from Chess.com API
data = []
# for player in ["magnuscarlsen", "rpragchess"]:
for _player in ["doesn't matter"]:
    headers = {"x-key": "ENV_GIE_XKEY"}
    response = requests.get("https://agsi.gie.eu/api", headers=headers)
    response.raise_for_status()
    data.append(response.json())
# Extract, normalize, and load the data
info = pipeline.run(data, table_name="player")
info = pipeline.run(data, table_name="gas_storage")
logger.info(info)


headers = {"Accept": "application/json"}
response = requests.get("https://nautobot.demo.networktocode.com/api", headers=headers)
