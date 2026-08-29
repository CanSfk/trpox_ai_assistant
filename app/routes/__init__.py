from .ai_routes import ai_routes
from .page_routes import page_routes


# Duzenli bir yapi icin rotalari tek bir yerden yonetiyoruz\dahil ediyoruz.
def register_routes(app):
    app.register_blueprint(ai_routes)
    app.register_blueprint(page_routes)
