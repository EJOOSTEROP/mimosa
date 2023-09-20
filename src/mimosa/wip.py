"""Sample dlt pipeline.

Loads data from European Gas data REST API.

Loads data incrementally into DuckDB.
"""

from mimosa.pipelines import GEI

pipeline = GEI()
pipeline.run_landing_pipeline()
pipeline.run_reporting_pipeline()
