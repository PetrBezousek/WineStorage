"""Application startup script for production"""
from src.flask_app import create_app

# uwsgi needs a variable called application
application = create_app()
