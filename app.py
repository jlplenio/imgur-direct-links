from flask import Flask, render_template, request

from util import build_post_response

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# rate limiting
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10 per minute"],
    )


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return build_post_response(request)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
