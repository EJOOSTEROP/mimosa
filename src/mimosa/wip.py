"""Sample dlt pipeline.

Loads data from European Gas data REST API.

Loads data incrementally into DuckDB.
"""
from datetime import date  # F401

from mimosa.pipelines import GEI

pipeline = GEI(destination="motherduck")
reporting_update = False
pipeline.run_landing_pipeline(
    gas_date=date(2023, 9, 21),  # still from 2019-01-01 to 2019-09-01
    to_gas_date=date(2023, 9, 24),
    reporting_update=reporting_update,
)
pipeline.run_landing_pipeline(
    gas_date=date(2019, 1, 1),  # still from 2019-01-01 to 2019-09-01
    to_gas_date=date(2019, 9, 2),
    reporting_update=reporting_update,
)
if not reporting_update:
    pipeline.run_reporting_pipeline()
