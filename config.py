import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

# Check token
if not TELEGRAM_TOKEN or not OPENROUTER_API_KEY:
    raise ValueError("Not token in .env file!")