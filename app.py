from flask import Flask, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from dao import Dao
from util import build_post_response

app = Flask(__name__)
version = "v0.3"

# rate limiting
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10 per minute"],
    )

# data access object
dao = Dao()


@app.route('/', methods=['POST', 'GET'])
def index():
    render_parameters = {}

    if request.method == 'POST':

        render_parameters = build_post_response(request)
        if 'link_list' in render_parameters:
            dao.inc_counter("actions")

    return render_template('index.html',
                           actions=dao.get_counter("actions")[0][0],
                           version=version,
                           **render_parameters)


if __name__ == '__main__':
    app.run()
