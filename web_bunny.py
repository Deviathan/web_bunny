from flask import Flask, render_template, request 
import requests
global version,r
version = ("0.01")
app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html",version=version)

@app.route('/target' ,methods = ['POST','GET'])
def target():
    errors = []
    results = {}
    if request.method == "POST":
        try:
            url = request.form['url']
            r = requests.get(url)
            results = r.text
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
    return render_template('target.html',errors=errors, results=results)

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