
<img src="https://prasakis.com/github/sumarpi.png?new" width="160" align="right">

**Tech Stack**

[![Build Status](https://img.shields.io/badge/Build%20with-Python-9CF?&logo=python)](https://img.shields.io/badge/Build%20with-python-9CF) 
[![Build Status](https://img.shields.io/badge/Build%20with-Flask-blue)](https://img.shields.io/badge/Build%20with-python-9CF) 
[![Build Status](https://img.shields.io/badge/Build%20with-GenSim-yellow)](https://img.shields.io/badge/Build%20with-GenSim-green) 

**Social**

[![Built on](https://img.shields.io/badge/Personal-Website-Green)](https://prasakis.com/sumarpi) [![Built on](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/dimitrisprs/) 

# General

This is a demonstration project for <a href="https://squirro.com/"> Squirro </a>
 
Sumparpi is a RESTful API built on Flask and TinyDB, used in order to generate and retrieve the summary of large texts using the gensim NLP module. The API is consisted of two endpoints. 
- `/` where texts can be posted and 
- `/summary/<id>` where text summaries can be retrieved. 

*sumarPI is a wordplay derived from the phrase "Summary API"*

Table of Contents
=================

* [General](#general)
* [Installation](#installation) 
* [Tests](#tests)
* [To Do's](#to-do-testing)

# Installation

Prior installation, consider using a virtual enviroment
```sh
~$ virtualenv sumarpi_env
~$ source sumarpi_env/bin/activate
```
Install with

```sh
~$ git clone https://github.com/DimitrisPr/sumarpi.git
~$ cd sumarpi
~$ pip install .
```
Launch the Flask server using:

```sh
~$ sumarpi start
```
Visit http://127.0.0.1/ and POST your text using the form template

<img src="https://prasakis.com/github/sumarpi-template.png" width="650">

# Tests

Currently, there are four unit test scenarios implemented in SumarPI, that test the GET and POST HTTP response codes respectively.

```sh
~$ cd sumarpi
~$ python tests/test_API.py
```

## To Do Testing

Throughout testing should also include:

- More unit tests for the HTTP response codes (e.g 201 for newly created objects)
- Tests for different kind of text inputs (e.g null text, non-ASCII text, large texts etc)

## Understanding the architecture of SumarPI

The following table presents briefly each SumarPI submodule 

| File/Module | Brief description |
| ------ | ------ |
| sumarpi/api.py | This module contains the Flask application factory, including the configuration of the endpoints|
| sumarpi/models.py | This module implements the SumarPI's Document model. Please note that in a non-development enviroment the database should be registered using the global Flask.g.db |
| sumarpi/cli.py | This module contains the terminal client interface for launching the SumarPI server.|
| sumarpi/templates| This directory contains the Flask templates (the Form in this case).  |
| sumarpi/static | This directory contains the Flask static files used by the templates (e.g CSS, JS, images etc)|
| tests | This directory contains the SumarPI's tests. |


