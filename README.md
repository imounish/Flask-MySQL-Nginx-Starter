# Flask-MySQL-Nginx-Starter

A starter kit for running backend service using **Nginx**, **Flask**, and **MySQL** as Docker containers.  

## Description

This is a simple starter kit for initializing Flask application to run inside Docker container accessing MySQL running inside a container. The Nginx server running inside a container acts as a reverse proxy.  

| Container Name    | Description                                     |
|-------------------|-------------------------------------------------|
| backend           | Container to run flask application              |
| db                | Container to run a MySQL 5.7 Database           |
| nginx             | Container to run Nginx Server as reverse proxy  |  

The current docker-compose file sets up the development environment to work.  
However, to run the container in production, uncomment the lines specified in respective files and remove `backend/run.py`.  
The production environment uses *gunicorn* as a production WSGI HTTP server.  

## How to Use

Set up an `instance` directory in the project root folder and add a file `config.py`. This file is used to set configuration information for the Flask App instance.  
An example `instance/config.py` looks like

```python
import os

user = os.environ['MYSQL_USER']
password = ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
database = ['MYSQL_DATABASE']

SECRET_KEY = '<Enter your secret Key>'
SQLALCHEMY_DATABASE_URI = f'mysql://{user}:{password}@{host}/{database}'
```

The `.env` file should also be set up to export the environment variables to the docker container through docker-compose.yml.  

A sample `.env` file looks like  

```txt
MYSQL_USER = dt_admin
MYSQL_PASSWORD = dt2016
MYSQL_HOST = localhost
MYSQL_DATABASE = dreamteam_db
MYSQL_ROOT_PASSWORD_FILE = /run/secrets/db-password
```

The `/run/secrets/` is the location inside the docker container where the secrets are located.  

Also, set up a `/db/password.txt` file to store the root password.  

The `/db/init.sql` file consists of intialization code for the db container. All the database initialization steps (like creation of tables, giving permissions to users, etc.) can be run through this file.  

## Building and Starting the Containers

To start the containers, use

```bash
$ docker-compose up
```

To run in detached mode, use `-d` argument.  

To stop the containers, use

```bash
$ docker-compose down
```

To remove the volumes also, use `-v` argument.  
In case of interactive shell, use `ctrl+c` to gracefully close the running containers.

In case of any issues, delete the images corresponding to the container and restart everything using `docker-compose up`.  

### Accessing the Flask Application

The Flask application can be accessed through localhost from any web browser.  
