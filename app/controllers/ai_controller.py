from flask import request, jsonify

from app.services.ai_service import AiService


# Nesneyi olusturuyoruz
ai_service = AiService()


# Kullanicidan mesaji aliyoruz ve yanit donderiyoruz
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"error": "Message is required."}), 400

        message = data["message"]

        # AI servisinden yanıt alınıyor
        response = ai_service.chat(message)

        return jsonify({"response": response}), 200

    except Exception as e:
        # Beklenmeyen bir hata veya API çökmesi durumunda çalışır
        return jsonify(
            {"error": "An unexpected error occurred.", "details": str(e)}
        ), 500
