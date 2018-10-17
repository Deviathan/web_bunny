from flask import Flask, render_template 

app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",version="0.01")

@app.route('/target')
def target():
    return render_template('target.html')

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


    