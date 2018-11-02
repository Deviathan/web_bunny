from flask import Flask, render_template, request , jsonify
from forms import http_req_forms,href_finder
from bs4 import BeautifulSoup

from http_requests import post,put,get,option,delete,head
from href_find import findhref

import requests

global version,r,error,result,error_reply

request_headers , request_reply , request_text, error_reply = "","","",""

error = False

version = ("0.01")
app=Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"))

#index page
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html",version=version)

@app.route('/http_requester' ,methods = ['POST','GET'])
def http_requester():
    #gets input from forms (forms.py)/http_requester.html
    form = http_req_forms()
    #if Execute button is pressed runs
    if form.validate_on_submit():
        c_s = form.c_s.data
        request_type = form.req.data
        url = form.url.data
        cua = form.c_ua.data
        inua = form.in_ua.data
        global error , request_headers , request_reply , request_text , error_reply

        #calling post request (post.py)
        if (request_type=='POST'):
            r,request_headers,request_reply,request_text,error,error_reply= post(c_s,url,cua,inua)
            if (error == True):
                return render_template('http_requester.html',form=form,r=error_reply)
            elif(error == False):
                return render_template('http_requester.html',r=r,form=form, headers = request_headers, reply = request_reply ,text = request_text, url=url, req=request_type)
        #calling get request (get.py)
        if (request_type=='GET'):       
            r,request_headers,request_reply,request_text,error,error_reply= get(c_s,url,cua,inua)
            if (error == True):
                return render_template('http_requester.html',form=form,r=error_reply)
            elif(error == False):
                return render_template('http_requester.html',r=r,form=form, headers = request_headers, reply = request_reply ,text = request_text, url=url, req=request_type)
        #calling put request (put.py)
        if (request_type=='PUT'):
            r,request_headers,request_reply,request_text,error,error_reply= put(c_s,url,cua,inua)
            if (error == True):
                return render_template('http_requester.html',form=form,r=error_reply)
            elif(error == False):
                return render_template('http_requester.html',r=r,form=form, headers = request_headers, reply = request_reply ,text = request_text, url=url, req=request_type)
        #calling delete request (delete.py)
        if (request_type=='DELETE'):
            r,request_headers,request_reply,request_text,error,error_reply= delete(c_s,url,cua,inua)
            if (error == True):
                return render_template('http_requester.html',form=form,r=error_reply)
            elif(error == False):
                return render_template('http_requester.html',r=r,form=form, headers = request_headers, reply = request_reply ,text = request_text, url=url, req=request_type)
        #calling head request (head.py)
        if (request_type=='HEAD'):
            r,request_headers,request_reply,request_text,error,error_reply= head(c_s,url,cua,inua)
            if (error == True):
                return render_template('http_requester.html',form=form,r=error_reply)
            elif(error == False):
                return render_template('http_requester.html',r=r,form=form, headers = request_headers, reply = request_reply ,text = request_text, url=url, req=request_type)
        #calling options request (option.py)
        if (request_type=='OPTIONS'):
            r,request_headers,request_reply,request_text,error,error_reply= option(c_s,url,cua,inua)
            if (error == True):
                return render_template('http_requester.html',form=form,r=error_reply)
            elif(error == False):
                return render_template('http_requester.html',r=r,form=form, headers = request_headers, reply = request_reply ,text = request_text, url=url, req=request_type)
    return render_template('http_requester.html',form=form,r=error)


@app.route("/history" ,methods = ['POST','GET'])
def history():
    return render_template("history.html")

@app.route("/options" ,methods = ['POST','GET'])
def options():
    return render_template("options.html")

@app.route("/hreffinder" ,methods = ['POST','GET'])
def hreffinder():
    form = href_finder()
    global href
    href = []
    #if Execute button is pressed runs
    if form.validate_on_submit():
        url = form.url.data
        data = findhref(url).splitlines()
        href.extend(data)
        
    return render_template("href_finder.html",form = form,href=href , url = url)

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
