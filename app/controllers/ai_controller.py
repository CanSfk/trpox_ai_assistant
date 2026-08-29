from flask import request, jsonify

from app.services.ai_service import AiService


ai_service = AiService()


def chat():
    # data = request.get_json()

    # if not data or "message" not in data:
    #     return jsonify({"error": "Message is required."}), 400

    # message = data["message"]

    message = "Hello, how are you"

    response = ai_service.chat(message)

    return jsonify({"response": response}), 200
