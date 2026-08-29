import os

# env dosyasini dahil ediyoruz
from dotenv import load_dotenv


# env dosyasini yukluyoruz
load_dotenv()


# Api anahtar degerimizi aliyoruz.
AI_API_KEY = os.getenv("AI_API_KEY")

# Eger anahtar deger yok ise hata firlatiyoruz
if not AI_API_KEY:
    raise ValueError("AI_API_KEY is not configured.")
