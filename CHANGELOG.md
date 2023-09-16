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
- dlt pipeline to load GIE EU gas data into DuckDB
    - load load_info (lineage related) data into destination database
- dbt structure for data transformations

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
