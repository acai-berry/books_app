# Bookstore application
A simple CRUD API application built with FastAPI. The application allows to add, delete, update and view books. Additionally, the functionality to search in titles using keywords is provided.

## Installting/getting started

This application is dockerized, to start up docker container use $ docker-compose up.


## Developing

### Built With

* Python 3.10
* FastAPI 0.79.1
* SQLAlchemy 1.4.40

detailed information on other libraries used can be found in Pipfile.lock.

### Prerequisites

* Python 3.10 - https://www.python.org/downloads/
* Pipenv - https://pipenv.pypa.io/en/latest/

### Setting up Dev

To develop this application further:
1. clone this repository - git clone https://github.com/akasztalska/books_app.git
2. start up local environment - pipenv shell
	
## Tests

Tests are written using pytest library. 
To run tests use command: pytest

## Style guide

The style is checked by linter - flake8 and formatter - black. To check the configuration, read pre-commit-config.yaml. Pre-commit hook is added and code style checked before each commit.

## API reference

To check API documentation go to localhost:8000/docs

The application should run on localhost:8000. The available endpoints are:
 - / - GET, POST
 - /{book_id} - GET, PUT, DELETE
 - /search - GET (searching by keyword)
 
 ## Database
 
 Project uses SQLite database.
