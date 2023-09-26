"""Entry point for mimosa package command line interface.

A minimal modern data stack with working data pipelines in a single Docker container.
"""
from loguru import logger

from mimosa.pipelines import GEI


def main():
    """Entry Point.

    Also used as entry point by Google Cloud Function.
    """
    logger.debug("mimosa starting.")

    capture_gas_data(
        destination="motherduck", gas_date=None, to_gas_date=None, reporting_update=True
    )

    logger.debug("mimosa completed.")

    return -1


def capture_gas_data(
    destination="motherduck", gas_date=None, to_gas_date=None, reporting_update=True
):
    """Run the pipeline to process data for a specific destination.

    With default values the pipeline will request the latest available data. Will store the results in a
    motherduck database. And will run the reporting pipeline.

    Parameters:
        destination (str): The database type where to capture the data. Defaults to "motherduck".
        gas_date (datetime): The starting date for requesting the data. Defaults to None.
        to_gas_date (datetime): The ending date for requesting the data. Defaults to None.
        reporting_update (bool): Determines whether to perform reporting updates. Defaults to True.
    """
    pipeline = GEI(destination=destination)
    pipeline.run_landing_pipeline(
        gas_date=gas_date, to_gas_date=to_gas_date, reporting_update=reporting_update
    )


if __name__ == "__main__":
    main()
