"""One Class or Classes that each degine a dlt data loading pipeline.

For example a class that loads data from European Gas data REST API.
"""
import datetime
import os

import dlt
from dlt.sources.helpers import requests
from dotenv import find_dotenv, load_dotenv
from loguru import logger

_ = load_dotenv(find_dotenv())


class GEI:
    """Defines data loading pipeline for GEI gas storage data.

    It lands data from the European Gas data REST API into a landing/staging area, then can run the reporting pipeline.
    """

    def __init__(self):
        """Initializes the pipeline."""
        self.ENV_GIE_XKEY = os.getenv("ENV_GIE_XKEY")
        self.api_url = "https://agsi.gie.eu/api"
        self.api_headers = {"x-key": self.ENV_GIE_XKEY}

        self.timing_key = "gasDayStart"
        self.primary_key = ("gasDayStart", "code")

        self.pipeline_name = "gas_storage"
        # credentials for the destination may be required
        self.destination = "motherduck"  # "duckdb" "motherduck"

    @dlt.resource(
        primary_key=("gasDayStart", "code"),
        table_name="storage",
        write_disposition="merge",
    )
    def _get_storage_data(
        self,
        created_at=dlt.sources.incremental("gasDayStart", initial_value="2023-07-10"),
        gas_date=None,
    ):
        """Gets storage data from a REST API.

        It is assumed that the API responsed contains a "data" field. The data field is a list of dictionaries.

        Returns: Yields the data field of the JSON response.
        """
        api_query = f"date={gas_date.strftime('%Y-%m-%d')}" if gas_date else ""

        url = f"{self.api_url}?{api_query}"
        logger.debug(url)

        # TODO: the pagination is not working
        while True:
            response = requests.get(url, headers=self.api_headers)
            response.raise_for_status()
            logger.debug(response)
            yield response.json().get("data")

            # stop requesting pages if the last element was already older than initial value
            # note: incremental will skip those items anyway, we just do not want to use the api limits
            # TODO: out of range does not work
            if created_at.start_out_of_range:
                break

            # get next page. TODO: Review the GIE API spec to confirm whether this is supported.
            if "next" not in response.links:
                break
            url = response.links["next"]["url"]

    def run_landing_pipeline(self):
        """Runs the landing pipeline."""
        pipeline = dlt.pipeline(
            pipeline_name=self.pipeline_name,
            destination=self.destination,
            dataset_name="landing",
        )

        # Run pipeline
        load_info = pipeline.run(
            self._get_storage_data(
                self,
                gas_date=datetime.datetime.strptime(
                    "2023-08-09", "%Y-%m-%d"
                ).astimezone(),
            )
        )
        row_counts = pipeline.last_trace.last_normalize_info

        # Load lineage and run related info into destination
        pipeline.run([load_info], table_name="_load_info")

        # Log outcome
        logger.debug(row_counts)
        logger.debug(load_info)

    def run_reporting_pipeline(self):
        """Runs the reporting pipeline."""
        pipeline = dlt.pipeline(
            pipeline_name=self.pipeline_name,  # Changing pipeline name causes errors. Maybe try with source.yml.
            destination=self.destination,
            dataset_name="reporting",  # Different target schema.
        )

        venv = dlt.dbt.get_venv(pipeline)

        # get runner, optionally pass the venv
        dbt = dlt.dbt.package(pipeline, "/workspaces/mimosa/etc/dbt/gie", venv=venv)

        models = dbt.run_all()

        # on success print outcome
        for m in models:
            logger.info(
                f"Model {m.model_name} materialized "
                f"in {m.time} "
                f"with status {m.status} "
                f"and message {m.message}."
            )


# TODO: Cannot load earlier dates. Not sure if i should update the 'created_at' field to something else than 'gas_day_start'.
