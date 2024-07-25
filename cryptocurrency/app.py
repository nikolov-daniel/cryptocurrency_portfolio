from cryptocurrency import create_app
from flask import Flask
import requests
import argparse
import json
from cryptocurrency.blueprint import blueprint
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Numeric, DateTime, VARCHAR
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime
import time

from cryptocurrency.model.transaction import Transactions
from cryptocurrency.model.user import User

app = create_app('dev')
app.app_context().push()


app.register_blueprint(blueprint)
app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True)
