import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from routes import init_routes
from get_time import get_time


def create_app(test_config=None):
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", 5432)
    database_name = os.getenv("POSTGRES_DATABASE_NAME", "mydb")
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")

    # creates an application that is named after the name of the file
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "some_dev_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{database_name}"
    # f"postgresql://{user}:{password}@pgsql:{port}/{database_name}"

    # initializing routes
    init_routes(app)

    return app


app = create_app()
# # bootstrap database migrate commands
# db.init_app(app)
# migrate = Migrate(app, db)


db = SQLAlchemy(app)
# db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
