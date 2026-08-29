from flask import Blueprint

from app.controllers.ai_controller import chat

# Rotalari grupluyoruz.
ai_routes = Blueprint("chat", __name__)

# HTTP isteklerini ilgili methodlara yonlendiriyoruz
# ai_routes.route("/chat", methods=["POST"])(chat)
ai_routes.route("/chat", methods=["GET"])(chat)
