import os

from dotenv import load_dotenv
load_dotenv()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return ""

@app.route('/status')
def status():
    return ""