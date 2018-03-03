from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/process_image')
def process_image():
  image_url = request.args.get('image', None, type=str)

