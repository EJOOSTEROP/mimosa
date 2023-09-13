"""Sample dlt pipeline."""
import os

import dlt
from dlt.sources.helpers import requests
from dotenv import find_dotenv, load_dotenv
from loguru import logger

_ = load_dotenv(find_dotenv())

logger.debug(os.getenv("ENV_GIE_XKEY"))

# Create a dlt pipeline that will load
# chess player data to the DuckDB destination
pipeline = dlt.pipeline(
    pipeline_name="chess_pipeline", destination="duckdb", dataset_name="player_data"
)
# Grab some player data from Chess.com API
data = []
for player in ["magnuscarlsen", "rpragchess"]:
    response = requests.get(f"https://api.chess.com/pub/player/{player}")
    response.raise_for_status()
    data.append(response.json())
# Extract, normalize, and load the data
info = pipeline.run(data, table_name="player")
logger.info(info)
