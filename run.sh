#!/bin/sh
export FLASK_APP="run.py"
source .env/bin/activate
flask run -h 0.0.0.0