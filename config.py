import os

from dotenv import load_dotenv


load_dotenv()


AI_API_KEY = os.getenv("AI_API_KEY")

if not AI_API_KEY:
    raise ValueError("AI_API_KEY is not configured.")
