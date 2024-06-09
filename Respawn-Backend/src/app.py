from flask import Flask, Response
from flask_cors import CORS

app = Flask(__name__, static_url_path='')
CORS(app)

# Test if the flask connection is running
@app.route('/')
def welcome_test():
    # Test that route is working
    return Response('Running on PORT: 5000')