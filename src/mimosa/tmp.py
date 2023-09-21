"""Temporary snippets."""
from mimosa.pipelines import GEI

pipeline = GEI(destination="motherduck")
reporting_update = False

if not reporting_update:
    pipeline.run_reporting_pipeline()
