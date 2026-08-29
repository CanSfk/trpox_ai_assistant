from groq import Groq

import config


# AiService sinifi.
class AiService:
    # Yapici method, sinif cagrildiginda ilk olarak calisir.
    def __init__(self):
        self.client = Groq(api_key=config.AI_API_KEY)

    # Kullanici mesajini yapay zekaya iletir ve yanit dondurur.
    def chat(self, message: str) -> str:
        response = self.client.chat.completions.create(
            model=config.AI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": config.AI_SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],
            max_tokens=config.AI_MAX_TOKENS,
            temperature=config.AI_TEMPERATURE,
        )

        return response.choices[0].message.content or "Not response"
