import os


GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyDkWk7PK3xGe5uE2ThlrQlgjnNegifhPlI")
GEMINI_MODEL_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
TEMPERATURE = 0.3