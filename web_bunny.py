from flask import Flask, render_template

from forms import http_req_forms,href_finder
from http_requests import http_requests
from href_find import findhref

global version,error

error = False
version = ("0.01")

app=Flask(__name__)

#needs to be configured ...in the near future :)
app.config.update(dict(
    SECRET_KEY= "powerful secretkey",
    WTF_CSRF_SECRET_KEY= "a csrf secret key"))

#index page
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html",version=version)

#/http_requester
@app.route('/http_requester' ,methods = ['POST','GET'])
def http_requester():
    #gets input from forms (forms.py)/http_requester.html
    form = http_req_forms()
    #When Execute button is pressed :
    if form.validate_on_submit():
        but = True 
        c_s = form.c_s.data
        request_type = form.req.data
        url = form.url.data
        cua = form.c_ua.data
        inua = form.in_ua.data
        global error , request_headers , request_reply , request_text , error_reply , r
        #http_requests.py
        r,request_headers,request_reply,request_text,error,error_reply= http_requests(c_s,request_type,url,cua,inua)
        if (error == True):
            return render_template('http_requester.html',form=form,r=error_reply)
        elif(error == False):
            return render_template('http_requester.html',r=r,form=form, headers = request_headers, reply = request_reply ,text = request_text, url=url, req=request_type,but=but)

    return render_template('http_requester.html',form=form,r=error)

#/href_finder
@app.route("/href_finder" ,methods = ['POST','GET'])
def hreffinder():
    form = href_finder()
    global href,url,buthref
    buthref = False
    url = ""
    href = []
    #When Execute button is pressed :
    if form.validate_on_submit():
        buthref = True 
        url = form.url.data
        data = findhref(url).splitlines()
        href.extend(data)
    return render_template("href_finder.html",form = form,href=href , url = url,but=buthref)

#/cms detection
@app.route("/cms_detection" ,methods = ['POST','GET'])
def cms_detection():
    form = href_finder()
    global href,url,buthref
    buthref = False
    url = ""
    href = []
    #When Execute button is pressed :
    if form.validate_on_submit():
        print("")
    return render_template("cms_detection.html",form = form,href=href , url = url,but=buthref)

#/history
@app.route("/history" ,methods = ['POST','GET'])
def history():
    return render_template("history.html")

#/options
@app.route("/options" ,methods = ['POST','GET'])
def options():
    return render_template("options.html")



#error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'),404

#error page
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('internal_error.html'),500

if __name__ == '__main__':
    app.run(debug="True")
