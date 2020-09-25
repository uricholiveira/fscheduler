## Default Flask Application, built in Factory Pattern
![GitHub issues](https://img.shields.io/github/issues/uricholiveira/flask-pattern.svg) 
![GitHub stars](https://img.shields.io/github/stars/uricholiveira/flask-pattern.svg) 

This repository contains the necessary to start with Flask API.

## Overview

In this application, we use the following plugins:
- [Flask-RestX](https://github.com/python-restx/flask-restx)
- [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate)
- [Flask-Marshmallow](https://github.com/marshmallow-code/flask-marshmallow)
- [Flask-SQLAlchemy](https://github.com/pallets/flask-sqlalchemy)
- [Dynaconf](https://github.com/rochacbruno/dynaconf)
- [Click](https://github.com/pallets/click)
* and others.. full list of all plugins *here*

## Getting Started
### Install dependencies:
All dependencies is in **requirements.txt**, using pip to install:
`pip install -r requirements.txt`

### Configure .env and settings.toml:
#### .env
You can define ***environments variables***, just modify it.

#### settings.toml
Here are the most usable *configurations* of the application, it is used by [Dynaconf]() plugin. <br />

According to **FLASK_ENV**, the plugin will search for the information contained in the **settings.toml**. <br />
* [default] -> is top level configuration, here is always instanced.
* [production] -> depends of **FLASK_ENV**
* [development] -> depends of **FLASK_ENV**
* [testing] -> depends of **FLASK_ENV**

To see more, please visit Dynaconf [documentation](https://www.dynaconf.com/).

### Run the application
To run application, a series of steps are required:
1. `flask db init` to start the *migrations* of your database.
2. `flask db migrate` to migrate your changes.
3. `flask db upgrade` to persist and create your database.

And if everything goes well, the last command is: `flask run`

Finally, be happy and let's code!

Thank you, and if you have a feedback, please send me a private message :)
