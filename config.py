import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("API_TOKEN")
CHAT_ID = os.getenv('CHAT_ID')
THREAD_ID = os.getenv('THREAD_ID')
# ALLOWED_IDS = os.getenv('ALLOWED_IDS').split(',')
# ALLOWED_IDS = [int(id) for id in ALLOWED_IDS]
CURRENCY = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "TONUSDT", "SUIUSDT"]
