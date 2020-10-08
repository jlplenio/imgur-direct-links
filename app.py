from flask import Flask, render_template, request

from util import build_post_response

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return build_post_response(request)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
