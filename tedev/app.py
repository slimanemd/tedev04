from flask import Flask


# initialization
from tedev.config import SECRET_KEY


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    return app

#
app = create_app()

# routes
@app.route('/')
def index():
    return 'Hello World new message hello again by me again encore'
