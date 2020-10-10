import os

from flask import Flask, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from dao import Dao
from util import get_links, handle_extras

app = Flask(__name__)
version = "v0.4"

# rate limiting
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["15 per minute"],
    )

# data access object
dao = Dao()


@app.route('/', methods=['POST', 'GET'])
def index():
    render_parameters = {}

    if request.method == 'POST':
        if 'button_get_links' in request.form:
            render_parameters = get_links(request)
            # if 'link_list' in render_parameters:
            #     dao.inc_counter("actions")
        elif 'button_extra' in request.form.keys():
            render_parameters = handle_extras(request)

    return render_template('index.html',
                           actions=dao.get_counter("actions")[0][0],
                           version=version,
                           **render_parameters)


if __name__ == '__main__':
    if os.environ.get('flask_debug'):
        app.debug = True
    app.run()
