from flask import Flask, render_template, request
from forms import url_form
import requests
import BeautifulSoup
global version,r


version = ("0.01")
app=Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"))


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html",version=version)

@app.route('/target' ,methods = ['POST','GET'])
def target():
    form = url_form()
    if form.validate_on_submit():
        print("")
    return render_template('target.html',form=form)

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/options")
def options():
    return render_template("options.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('internal_error.html'),500

if __name__ == '__main__':
    app.run(debug="True")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)