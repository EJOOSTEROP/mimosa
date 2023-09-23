"""Entry point for mimosa package command line interface.

A minimal modern data stack with working data pipelines in a single Docker container.
"""
from mimosa.pipelines import GEI


def main():
    """_summary_."""
    print("Hello world from mimosa.")  # noqa T201

    pipeline = GEI(destination="motherduck")
    pipeline.run_landing_pipeline()

    return -1


if __name__ == "__main__":
    main()
