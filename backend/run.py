"""
Only to be used in development environment
Enables debug mode and reloading
"""
import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=5000)