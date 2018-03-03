from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from ocr import process_image

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/process')
def process():
  image_url = request.args.get('image')
  res = process_image(image_url)
  return jsonify(list(res))

@app.route('/test')
def test():
  return request.args.get('test')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int('80'))