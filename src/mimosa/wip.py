"""Sample dlt pipeline.

Loads data from European Gas data REST API.

Loads data incrementally into DuckDB.
"""

from datetime import date  # F401

from mimosa.pipelines import GEI

destination = "motherduck"  # "filesystem" "motherduck"
pipeline = GEI(destination=destination)
reporting_update = False

run_this = True
if run_this:
    pipeline.run_landing_pipeline(
        gas_date=date(2024, 2, 15),  # still from 2019-01-01 to 2019-09-01
        to_gas_date=date(2024, 2, 16),
        reporting_update=reporting_update,
    )
    """
    pipeline.run_landing_pipeline(
        reporting_update=reporting_update,
    )
    """
else:
    if destination == "motherduck":
        pipeline.run_landing_pipeline(reporting_update=reporting_update)
    else:
        pipeline.run_landing_pipeline(reporting_update=False)

if not reporting_update and destination == "motherduck":
    pipeline.run_reporting_pipeline()
