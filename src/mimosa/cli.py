"""Entry point for mimosa package command line interface.

A minimal modern data stack with working data pipelines in a single Docker container.
"""
from mimosa.pipelines import GEI


def main():
    """Entry Point.

    Also used as entry point by Google Cloud Function.
    """
    print("Hello world from mimosa.")  # noqa T201

    pipeline = GEI(destination="motherduck")
    pipeline.run_landing_pipeline()

    print("mimosa completed.")  # noqa T201

    return -1


def main_does_work():
    """_summary_."""
    print("Hello world from mimosa helper.")  # noqa T201

    pipeline = GEI(destination="motherduck")
    print("Starting the simple reportig pipeline.")  # noqa T201
    pipeline.run_reporting_pipeline()
    print("Completed the simple reportig pipeline.")  # noqa T201


if __name__ == "__main__":
    main()
