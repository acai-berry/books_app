# Bookstore application
A simple CRUD API application with FastAPI.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This application is built using FastAPI, SQLAlchemy and uses SQLite. The application is dockerized and pre-commit hook is added.


## Technologies
Project is created with:
* Python 3.10
* FastAPI 0.79.1
* SQLAlchemy 1.4.40

detailed information on other libraries used can be found in Pipfile.lock.
	
## Setup
To start up docker container use $ docker-compose up -d


The application should run on localhost:8000. The available endpoints are:
 - / - GET, POST
 - /{book_id} - GET, PUT, DELETE
