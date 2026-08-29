import config
from flask import Flask

from app.routes import register_routes
from flask_cors import CORS

debug_state = bool(config.DEBUG)


def create_app():
    app = Flask(__name__, template_folder="./app/templates")

    if debug_state:
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
        debug=debug_state,
    )
