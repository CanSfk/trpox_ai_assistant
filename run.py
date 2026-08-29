import config
from flask import Flask

from app.routes import register_routes
from flask_cors import CORS


def create_app():
    app = Flask(__name__, template_folder="app/templates")

    if config.DEBUG:
        CORS(app)
    else:
        CORS(app, resources={r"/*": {"origins": "https://trpox.com"}})

    register_routes(app)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=config.DEBUG,
    )
