<!-- Inspired by https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md -->

<a name="readme-top"></a>


<!-- SHIELDS HEADER -->
<div align="center">


[![contributors-shield]][contributors-url] [![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url] [![Issues][issues-shield]][issues-url] [![MIT License][license-shield]][license-url] [![LinkedIn][linkedin-shield]][linkedin-url]

[contributors-shield]: https://img.shields.io/github/contributors/EJOOSTEROP/mimosa.svg?logo=github
[contributors-url]: https://github.com/EJOOSTEROP/mimosa/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/EJOOSTEROP/mimosa.svg?logo=github
[forks-url]: https://github.com/EJOOSTEROP/mimosa/network/members

[stars-shield]: https://img.shields.io/github/stars/EJOOSTEROP/mimosa.svg?logo=github
[stars-url]: https://github.com/EJOOSTEROP/mimosa/stargazers

[issues-shield]: https://img.shields.io/github/issues/EJOOSTEROP/mimosa.svg?logo=github
[issues-url]: https://github.com/EJOOSTEROP/mimosa/issues

[license-shield]: https://img.shields.io/github/license/EJOOSTEROP/mimosa.svg?logo=github
[license-url]: https://github.com/EJOOSTEROP/mimosa/blob/main/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/erik-oosterop-9505a21

[![current release](https://img.shields.io/github/release/ejoosterop/mimosa.svg)](https://github.com/ejoosterop/mimosa/releases)

<!-- no PyPi repository
[![PyPI - Python Version][pypi-python-shield]][https://pypi.org/project/x_mimosa_x]

[pypi-python-shield]: https://img.shields.io/pypi/pyversions/mimosa?logo=python


[![PyPi - Package Version][pypi-version-shield]][https://pypi.org/project/x_mimosa_x]

[pypi-version-shield]: https://img.shields.io/pypi/v/mimosa?logo=python


[![PyPi - License][pypi-license-shield]][license-url]

[pypi-license-shield]: https://img.shields.io/pypi/l/mimosa?logo=python
-->
</div>

<!-- PROJECT SUMMARY AND LOGO -->
<div align="center">
  <a href="https://github.com/EJOOSTEROP/mimosa">
    <img src="https://github.com/EJOOSTEROP/mimosa/blob/main/etc/logo.png?raw=true" alt="Logo" width="180" height="180">
  </a>

<h3 align="center">mimosa</h3>

  <p align="center">
    The ELT part of a modern data stack with working data pipelines using cloud functionality.
    <br />
    <a href="https://github.com/EJOOSTEROP/mimosa"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!--
    <a href="https://github.com/EJOOSTEROP/mimosa">View Demo</a>
    ·
    -->
    <a href="https://github.com/EJOOSTEROP/mimosa/issues">Report Bug</a>
    ·
    <a href="https://github.com/EJOOSTEROP/mimosa/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<br />
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
      <!-- <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul> -->
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ABOUT THE PROJECT -->
## About the Project

<div  align="center">
  <a href="https://github.com/EJOOSTEROP/mimosa">
    <img src="https://github.com/EJOOSTEROP/mimosa/blob/main/etc/intro_image.jpg?raw=true" alt="intro_image" width="75%" height="75%">
  </a>
</div>

<div>

<br /><br />
The ELT part of a modern data stack with working data pipelines using cloud functionality. This is similar in concept to [mimodast][mimodast-repo-url] using alternative software options and cloud functionality.
<!-- MIMOdast Software Alternatives -->

Mimosa contains the ELT (extract load transform) part used to publish a webpage at [gas.aspireto.win][aspireto-gas-url] that reports on natural gas storage in the European Union. The process captures data from a REST API and stores it in a database after transforming the data for reporting pusposes.

The REST API is published by [Gas Infrastructure Europe][GIE-URL].

Apart from the gas storage information this repository is useful as an exploration of the tools involved:
- [dlt][dlthub-url] for data loading
- [dbt][dbt-url] for transformation
- [MotherDuck][motherduck-url] for storing the data in a cloud based [DuckDB][DuckDB-url] database.

The <a href="#Tech Stack">full tech stack</a> used to create the [gas.aspireto.win][aspireto-gas-url] is detailed below.

<img src="https://github.com/EJOOSTEROP/mimosa/blob/main/etc/web_print.png?raw=true" alt="Logo" width="35%" height="35%">

</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- BUILT WITH -->
<!--
### Built With

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- GETTING STARTED -->
## Getting Started

<!--To get a local copy up and running follow these simple example steps.
-->

Link to https://gas.ternyx.com
- pip install ternyxmimosa
- how to call from command line
- how to call from within Python
- requirements for secrets in environment variables
Steps involved in my deploy of the pipeline.

### Prerequisites

Setup a Python development environment.

### API Keys

Ensure the following secrets are specified in environment variables exist (or use .env file):
- To access the [GIE Gas Inventory][GIEAPI-url] REST API an API key is required. Create a free and immediate [GIE account][GIEAccount-url] to obtain the key. Expose it in the folling env variable:
  - ENV_GIE_XKEY = "YOUR-API-KEY"
- The [service token][motherduck-token-url] and database name used for MotherDuck:
  - DESTINATION__MOTHERDUCK__CREDENTIALS = "md:///YOUR-DATABASE-NAME?token=YOUR-SERVICE-TOKEN"
  - Note that the [MotherDuck][motherduck-url] page uses a different format. The above format is required for [dlt][dlthub-url].


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation

Execute the following command. Consider using a venv.
```shell
pip install ternyxmimosa
```

Alternatively clone this repository. Or pip install from GitHub.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

### Tech Stack
The notebook is built using the [evidence](https://evidence.dev/) reporting tool. The notebooks are contained in the current GitHub [repository](https://github.com/EJOOSTEROP/gie-evidence-dash).

The data is obtained using a REST API from [GIE](https://agsi.gie.eu/). [dlt Hub](https://dlthub.com/) and [dbt](https://www.getdbt.com/) are used to load this data into a [MotherDuck](https://motherduck.com/) hosted database. This ELT process is run as a Google Cloud [Function](https://cloud.google.com/functions) triggered twice a day by a [schedule](https://cloud.google.com/scheduler).

A GitHub workflow builds the static evidence based notebook on a schedule (twice daily) and updates the webhost using ftp for the updated data to be reflected at [gas.aspireto.win](https://gas.aspireto.win).

NOTE: As of November 2023 it is possible to fully deploy this stack using free tiers of the cloud services used.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

<div>
Consider:

- [x] Get source data (Using REST API)
- [x] Transform data, possibly SQL Mesh or dbt.
  - [ ] Create data vault transformations (https://automate-dv.readthedocs.io/en/latest/).
- [ ] dlt update/error messages using Slack
- [x] Storage (currently local DuckDB, maybe consider some cloud alternative. Though that would stray from the data stack in a Docker concept.) (MotherDuck)
- [x] Scheduling Tool (Google Cloud Scheduler)
- [x] Reporting tool (Metabase?) (Evidence.dev in separate repository)
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

<!-- Contributions are what make the open source community such an amazing place to learn, inspire, and create. -->
Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also [open](https://github.com/EJOOSTEROP/mimosa/issues/new/choose) a feature request or bug report.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
<!--
## License

Distributed under the MIT License. See `LICENSE.txt` for more information. The tools and the sample data are subject to their own respective licenses.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- CONTACT -->
## Contact

<!--
Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com
-->

Project Link: [mimosa](https://github.com/EJOOSTEROP/mimosa)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
<!--
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>

-->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[aspireto-gas-url]: https://gas.aspireto.win

[mimodast-repo-url]: https://github.com/EJOOSTEROP/mimodast
[dlthub-url]: https://dlthub.com/
[dbt-url]: https://www.getdbt.com
[motherduck-url]: https://motherduck.com/
[motherduck-token-url]: https://motherduck.com/docs/authenticating-to-motherduck/#authentication-using-a-service-token
[DuckDB-url]: https://duckdb.org

[GIE-URL]: https://www.gie.eu/
[GIEAPI-url]: https://agsi.gie.eu/
[GIEAccount-url]: https://agsi.gie.eu/account