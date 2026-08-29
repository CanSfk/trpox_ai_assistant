# TRPOX AI Assistant

TRPOX AI Assistant, TRPOX için geliştirilen yapay zeka destekli bir asistandır.

Lojistik, taşımacılık ve planlama operasyonlarında kullanıcıya yardımcı olmak amacıyla geliştirilmektedir.

## Teknolojiler

- Python
- Flask
- Groq API
- Jinja2
- Gunicorn

## Proje Yapısı

```text
trpox_ai_assistant/
├── app/
│   ├── config/
│   ├── controllers/
│   ├── routes/
│   ├── services/
│   └── templates/
├── tests/
├── .env
├── .env.example
├── requirements.txt
├── run.py
└── README.md
```

## Kurulum

Virtual environment oluşturun:

```bash
python -m venv .venv
source .venv/bin/activate
```

Bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

`.env` dosyasını oluşturun:

```env
GROQ_API_KEY=your_api_key
DEBUG=true
```

## Çalıştırma

```bash
python run.py
```

Uygulama:

```text
http://127.0.0.1:5000
```

adresinde çalışır.

## Production

Production ortamında Gunicorn kullanılır:

```bash
gunicorn run:app
```

## Durum

Proje aktif olarak geliştirilmektedir.
