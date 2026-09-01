import sys
import os

# Add web_app folder to sys.path so Vercel can find app and data_engine modules
web_app_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../web_app"))
if web_app_dir not in sys.path:
    sys.path.append(web_app_dir)

from app import app

# Export app variable for WSGI serverless runtime
