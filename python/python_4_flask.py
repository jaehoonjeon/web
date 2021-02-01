# https://github.com/pallets/flask
# $ pip install -U Flask

# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"

"""
환경변수 등록
set FLASK_APP=python_4_flask.py
flask 실행
flask run

"""

