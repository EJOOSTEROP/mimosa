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
    The ELT part of a modern data stack with practical data pipelines using cloud functionality.
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
        <li><a href="#api-keys">API Keys</a></li>
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
    <img src="https://github.com/EJOOSTEROP/mimosa/blob/main/etc/intro_image.jpg?raw=true" alt="intro_image" width="75%" height="75%" title="AI generated image. Misleading image showing above ground gas storage facilities.">
  </a>
</div>

<div>

<br /><br />
The ELT part of a modern data stack with practical data pipelines and reporting using cloud functionality. This is similar in concept to [mimodast][mimodast-repo-url] using alternative software options and cloud functionality.
<!-- MIMOdast Software Alternatives -->

Mimosa encompasses the ELT (extract load transform) components necessary to generate the webpage found at [gas.aspireto.win][aspireto-gas-url], providing detailed reports on natural gas storage volumes within the European Union. This process involves retrieving data from a REST API, transforming it, and storing it in a database tailored for reporting purposes.

The source data is published by [Gas Infrastructure Europe][GIE-URL] and exposed in a REST API.

Beyond gas storage data, Mimosa offers a hands-on experience with essential tools:
- 🚀 [dlt][dlthub-url] for smooth data loading.
- 🔍 [dbt][dbt-url] for powerful data transformation.
- ☁️ [MotherDuck][motherduck-url]  for storing the data in a cloud based [DuckDB][DuckDB-url] database.

Further the full tech stack used to create the [gas.aspireto.win][aspireto-gas-url] pages is detailed <a href="#tech-stack">below</a>.
</div>

<br />

<div>
  <a href="https://gas.aspireto.win">
  <img src="https://github.com/EJOOSTEROP/mimosa/blob/main/etc/web_print.png?raw=true" alt="Screenshot of gas reporting at https://gas.apireto.win." width="75%" height="75%">
  </a>
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

### Prerequisites

Setup a Python development environment.

### API Keys

Ensure the following sensitive information is securely stored in environment variables or within a .env file:

- To access the [GIE Gas Inventory][GIEAPI-url] REST API, an API key is necessary. Quickly obtain your API key by signing up for a free [GIE account][GIEAccount-url]. Once acquired, expose it using the following environment variable:

  - ENV_GIE_XKEY = "YOUR-API-KEY"
- For [MotherDuck][motherduck-url], you'll need the [service token][motherduck-token-url] and the database name. Set up the following environment variables to establish the connection:

  - DESTINATION__MOTHERDUCK__CREDENTIALS = "md:///YOUR-DATABASE-NAME?token=YOUR-SERVICE-TOKEN"
  - Please note that the [MotherDuck][motherduck-url] page utilizes a different format, whereas the above format is specifically required for [dlt][dlthub-url].

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation

Execute the following command. Consider using a venv.
```shell
pip install ternyxmimosa
```

Alternatively clone this repository and use `poetry install`. Or pip install from GitHub.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

### Command Line
Not currently supported.

### As a Python Package

The following sample obtains the storage data for the last available date and stores it in MotherDuck.

```python
import mimosa.cli as GEI

GEI.main()
```

### Tech Stack

These are the technologies driving the content on [gas.aspireto.win][aspireto-gas-url]:
- **Google cloud** [function](https://cloud.google.com/functions) for the ELT component:
  - The function is a bare bones wrapper around the [mimosa][mimosa-repo-url] Python package (the current repository). The function is in this [repository][cloud-func-repo-url].
  - It is scheduled to run the ELT twice daily (using Google Scheduler and [Pub/Sub](https://cloud.google.com/pubsub) message).
  - The result is updated data in MotherDuck.
- **Reporting notebook**
  - Built using the [evidence](https://evidence.dev/) reporting tool, defined in this GitHub [repository](https://github.com/EJOOSTEROP/gie-evidence-dash).
  - Rebuild and published to a web host using a GitHub workflow.
    - Run on a twice daily schedule. The workflow is defined in the notebook [repository](https://github.com/EJOOSTEROP/gie-evidence-dash).


NOTE: As of November 2023 it is possible to fully deploy this stack without breaking the bank (using free tiers of the cloud services used). Dive into our GitHub repository and the linked ones for the Google Function and Evidence notebook, where all the code awaits. 🚀

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
- [ ] Bare bones CLI
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
[mimosa-repo-url]: https://github.com/EJOOSTEROP/mimosa
[cloud-func-repo-url]: https://github.com/EJOOSTEROP/gie-gcp-func
[dlthub-url]: https://dlthub.com/
[dbt-url]: https://www.getdbt.com
[motherduck-url]: https://motherduck.com/
[motherduck-token-url]: https://motherduck.com/docs/authenticating-to-motherduck/#authentication-using-a-service-token
[DuckDB-url]: https://duckdb.org

[GIE-URL]: https://www.gie.eu/
[GIEAPI-url]: https://agsi.gie.eu/
[GIEAccount-url]: https://agsi.gie.eu/account