from flask import Flask, render_template, request

from grabber import Grabber

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():

    # Todo: cut ur and check with ^[a-zA-Z0-9]{7}$

    if request.method == 'POST':
        link_list = ""
        message = ""
        imgur_url = request.form['imgur_url_field']
        try:
            link_list = Grabber.get_direct_links(imgur_url)
            link_list = [link+"\n" for link in link_list]
        except Exception as e:
            message = "There was an error " + str(e)
        return render_template('index.html',
                            link_list=link_list,
                            message=message,
                            imgur_url=imgur_url)
    else: 
        return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()