from flask import Blueprint

from app.controllers.ai_controller import chat

ai_routes = Blueprint("chat", __name__)

# ai_routes.route("/chat", methods=["POST"])(chat)
ai_routes.route("/chat", methods=["GET"])(chat)
