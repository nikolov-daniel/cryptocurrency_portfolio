from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from cryptocurrency.config.config import config_by_name
from flask_apscheduler import APScheduler
from cryptocurrency.service.crypto_service import save_prices


db = SQLAlchemy()

def scheduled():
    save_prices()
    #print("here")


def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[env_name])
    scheduler = APScheduler()
    with app.app_context():
        db.session.configure(autoflush=False)
        db.init_app(app)
        scheduler.init_app(app)

        scheduler.add_job(func=scheduled, trigger="interval", seconds=300000, id="crypto")

        scheduler.start()

    return app

