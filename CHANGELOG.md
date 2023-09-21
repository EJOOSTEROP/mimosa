# Changelog
All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [Unreleased]

## [0.0.1] 2023-09-13

### Added
- Setup core dependencies:
    - poetry add dlt
    - poetry add dlt[duckdb]
    - poetry add python-dotenv
    - poetry add loguru
    - poetry add streamlit
        - Temporary conflict with DuckDB version. Solved for now by fixing pandas to the latest (DuckDB) compatible version:
            - poetry add pandas=2.0.3
            - poetry add streamlit
        - Check back end of sep 2023 as the latest version of DuckDB should address this issue.
    - poetry add dlt[motherduck]
- dlt pipeline to load GIE EU gas data into DuckDB
    - load load_info (lineage related) data into destination database
    - materialize as table in dbt_project.yml
    - Re-create as class structure
- Adding motherduck as a destination.
- dbt structure for data transformations
    - Loading from source.yml loads all data in stage
    - loading from stage_gas_staging loads just the last dtl loaded data (as it is a dbt full load, just the new data is loaded)
    - Consider loading from stage_gas directly: should load everything again.
    - Consider using dbt incremental load

- LINKING NOTES:
    - stage_gas._load_info__loads_ids.value = storage._dlt_load_id

- PIPELINE DOES NOT LOAD ANY DATA ANYMORE. No code changes at all since last night; at least not that I realize.

### Dev Environment setup
- Mostly done using VS Code devcontainer and Poetry
- Separately:
    - pipx install dbt-duckdb --include-deps

### Fixed
- None

### Changed
- None

### Removed
- None
