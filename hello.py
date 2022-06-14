from waitress import serve
from flask import Flask
app = Flask(__name__)
serve(app, host='0.0.0.0', port=8080)