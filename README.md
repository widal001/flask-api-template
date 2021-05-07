# flask-api-template
Boiler plate code for a flask API with a db and Swagger documentation

## Table of Contents

- [About this Project](#overview)
  - [When to use this template](#when-to-use-this-template)
  - [When not to use this template](#when-not-to-use-this-template)
  - [Made With](#made-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Quick Installation](#quick-installation)
- [Usage](#usage)
- [Contributing](#contributing)

## About this Project

This is a template repo that contains boiler plate code for a flask API served by a PostgreSQL database. It is designed to provide a functional example of a project architecture that is lightweight yet robust and easily extensible. It also serves to reduce the headache of setting up some basic infrastructure for your API like auto-formatting, unit testing, documentation, and containerization.

### When to use this template

This template offers a good starting point for developers who are still new to designing and building APIs in Python, and for projects that require a simple but scalable architecture. The goal with this boiler plate code is to leverage some basic design patterns common to flask APIs, so that developers can focus on the functionality of their endpoints rather than on the reliability of the infrastructure.

### When _not_ to use this template

This template makes a series of opinionated choices about the project setup, namely in the selection of a relational database as the underlying datastore, SQLAlchemy as the ORM to interface with that datastore, and flask-restful as the framework for implementing a resource-driven API. If your project calls for a different set of architectural decisions, _and_ you're familiar enough with Flask enough to recognize the advantages of those alternatives, it likely easier to find a different template or start from scratch than it is to copy and adjust this template.

Likewise, the project setup is designed to support a Flask API but not an interactive frontend beyond the basic API documentation built on top of Swagger UI. For Flask applications that require a dedicated user interface in addition to, or in place of, an API, it would be best to find a different template that is optimized for managing templates, forms, and other frontend components.

### Made With

- [Docker](https://docs.docker.com/get-started/overview/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [flask restful](https://flask-restful.readthedocs.io/en/latest/)

## Getting Started

### Prerequisites

- Docker installed on your computer
- docker-compose installed on your computer

In order to check which version of python you have installed, run the following in your command line (for Mac/Linux)

> **NOTE:** in all of the code blocks below, lines preceded with `$` indicate commands you should enter in your command line (excluding the `$` itself), while lines preceded with `>` indicate the expected output from the previous command.

```
$ docker-compose -v && docker -v
> docker-compose version 1.28.5, build c4eb3a1f
> Docker version 20.10.5, build 55c4c88
```

If you don't have docker or docker-compose installed on your local machine, follow [these instructions to get docker](https://docs.docker.com/get-docker/)

### Quick Installation

1. Fork the repo following [these instructions](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo)
1. Clone the forked repo on your local machine`git clone https://github.com/YOUR_USERNAME/flask-api-template`
1. Run `docker-compose up -d` from the command line to build and run docker containers for the app. Something similar to the following should be printed to the console:
   ```
   $ docker-compose up -d          
   > Creating network "flask-api-template_default" with the default driver
   > Creating volume "flask-test-db" with default driver
   > Creating volume "flask-app-db" with default driver
   > Creating postgrestest ... done
   > Creating postgres     ... done
   > Creating app          ... done
   ```
1. Wait 2-3 seconds after the apps are built, then run `docker-compose exec app pytest` from the command line to execute the tests and ensure everything passes. Something similar to the following should be printed to the console:
   ```
   $ docker exec app pytest
   > =========================== test session starts ==========================
   > platform linux -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
   > rootdir: /app
   > plugins: dash-1.19.0
   > collected 5 items
   >
   > tests/api/test_indicator.py .                                       [100%]
   >
   > ============================ 5 passed in 4.32s ============================
   ```

## Usage

1. After you've cloned and installed the repo, run `docker-compose up -d` to start the app locally
1. Open a browser and go to [http://127.0.0.1:5000/api/docs](http://127.0.0.1:5000/api/indicators) and you should the Swagger UI page for the API.
1. When you're done using or testing the app tear down the containers by running `docker-compose down --volumes`

## Contributing

Details on contributing to the project TBD
