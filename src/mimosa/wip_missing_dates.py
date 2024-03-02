"""Sample dlt pipeline.

Loads data from European Gas data REST API.

Loads data incrementally into DuckDB for dates without data in the target schema.
"""

from datetime import date  # F401

import mimosa.dateswithoutdata as dwd
from mimosa.pipelines import GEI

destination = "motherduck"  # "filesystem" "motherduck"
pipeline = GEI(destination=destination)
reporting_update = False

for seq in dwd.tuples_of_missing_dates(start_dt=date(2022, 1, 15), end_dt=None):
    pipeline.run_landing_pipeline(
        gas_date=seq[0],
        to_gas_date=seq[1],
        reporting_update=reporting_update,
    )

# TODO: This also runs when no new data is added (when tuples_of_missing_dates yields no results).
if not reporting_update and destination == "motherduck":
    pipeline.run_reporting_pipeline()
