# /run.py
import os

from api.app import create_app

env_name = os.getenv('FLASK_ENV')
app = create_app('development')

if __name__ == '__main__':
    # Running app in debug mode
    app.run(debug=False)
