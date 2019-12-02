# Requirements
# python3.7, pip3
# REST API With Flask & SQL Alchemy

> Users API using Python Flask, SQL Alchemy and Marshmallow

## Quick Start Using Pipenv

``` bash
# install pipenv
$ pip3 install pipenv

# Activate venv
$ pipenv shell

# Install dependencies
$ pipenv install

# Create DB
$ python
>> from app import new_db
>> new_db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python app.py
```

## Endpoints

* GET     /users
* GET     /user/:id
* POST    /user
* PUT     /user/:id
* DELETE  /user/:id

# data JSON
{
    "email":"me@example.com",
    "firstname":"med",
    "lastname":"son",
    "birthdate":"2000-12-12 09:26:03.478039"
}
# for testing please use rest client (i used postman)
