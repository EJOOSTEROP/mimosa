"""Sample dlt pipeline.

Loads data from European Gas data REST API.

Loads data incrementally into DuckDB.
"""
from datetime import date  # F401

from mimosa.pipelines import GEI

pipeline = GEI(destination="duckdb")
pipeline.run_landing_pipeline(
    gas_date=date(2019, 1, 1), to_gas_date=date(2019, 1, 5), reporting_update=False
)
