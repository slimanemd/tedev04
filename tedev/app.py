from flask import Flask


# initialization
from tedev.config import SECRET_KEY, SQLALCHEMY_DATABASE_URI

from tedev.core.models.db_initializer import db, setup_db


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    setup_db(app)

    return app

#
app = create_app()

# routes
@app.route('/')
def index():
    return 'Hello World new message hello again by me again encore'
