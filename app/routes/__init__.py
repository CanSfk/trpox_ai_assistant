from .ai_routes import ai_routes


def register_routes(app):
    app.register_blueprint(ai_routes)
