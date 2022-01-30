"""Application startup script for development"""

import os

from src.flask_app import create_app

if __name__ == "__main__":
    os.environ["WERKZEUG_DEBUG_PIN"] = "off"
    create_app().run(host="0.0.0.0", port=4321, use_reloader=True, use_debugger=True)
