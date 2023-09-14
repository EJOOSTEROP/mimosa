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
    - ~~poetry add streamlit~~ While streamlit did work, the pipeline is broken afterwards. Uninstalling streamlit fixes that.
        - The problem is with Pandas (which installed with streamlit) and DuckDB.
        - Solved for now by fixing pandas to the latest compatible version:
            - poetry add pandas=2.0.3
            - poetry add streamlit
- dlt pipeline to load GIE EU gas data into DuckDB

### Fixed
- None

### Changed
- None

### Removed
- None
