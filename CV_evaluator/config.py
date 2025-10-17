import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file located next to this config.py (project root)
dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError(
        f"GEMINI_API_KEY environment variable is not set. "
        f"Searched .env at: {dotenv_path} and OS env. "
        f"If you are using a shell, set it in that shell or use setx to persist it."
    )

GEMINI_MODEL_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
TEMPERATURE = 0.3