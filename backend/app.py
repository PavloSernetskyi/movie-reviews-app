from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from routes import register_routes
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
