# Changelog
All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [Unreleased]

### Changed
- Cleanup logging messages.
- Fix DuckDB to v0.8.1 (v0.9 breaks motherduck)

## [0.0.10] 2023-09-25

### Changed
- Code cleanup.

## [0.0.6] 2023-09-24

### Added
- Additional logging, more frequent.

## [0.0.5] 2023-09-24

### Added
- Additional logging in landing and reporting pipeline

## [0.0.4] 2023-09-24

### Added
- Forcing reporting pipeline to run

## [0.0.3] 2023-09-24

### Added
- Logging entry for reporting pipeline

## [0.0.2] 2023-09-23

### Fixed
- dbt transform files are now included with the distribution package

## [0.0.1] 2023-09-23

### Added
- Initial version. Loads data from [GIE REST API](https://agsi.gie.eu/) into [motherduck](https://motherduck.com/).
- API key and motherduck token need to be set in environment variables, `ENV_GIE_XKEY` and `DESTINATION__MOTHERDUCK__CREDENTIALS` respectively.
- Published on pypi as [ternyxmimosa](https://pypi.org/project/ternyxmimosa/): `pip install ternyxmimosa`
- Within a Python code, use (for example): `import mimosa.cli as mimosa`

## [working_notes]

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
    - adding country reporting table - for annual consumption data
    - Consider loading from stage_gas directly: should load everything again.
    - Consider using dbt incremental load
- In pyproject.toml, set tool.poetry.name different from the packag name (add 'ternyx.' prefix)

- LINKING NOTES:
    - stage_gas._load_info__loads_ids.value = storage._dlt_load_id

- PIPELINE DOES NOT LOAD ANY DATA ANYMORE. No code changes at all since last night; at least not that I realize.
    - remove this logic: created_at=dlt.sources.incremental("gasDayStart", initial_value=
    - it solved it; but changing the initial_value date did not seem to have any positive impact.

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

