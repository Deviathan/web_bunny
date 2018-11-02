import requests

def post(c_s,url,cua,inua):
    try:
        if c_s == ("YES"):
            if cua == ("YES"):
                headers = {'user-agent': inua}
                s = requests.Session()
                r = s.post(url , headers=headers)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"

            else:
                s = requests.Session()
                r = s.post(url)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"
        elif c_s == ("NO"):
            if cua == ("YES"):
                headers = {'user-agent': inua}
                r = requests.post(url , headers=headers)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"

            else:
                r = requests.post(url)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"
    except requests.exceptions.Timeout as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        return r , request_headers , request_reply , request_text ,error , error_reply
    except requests.exceptions.TooManyRedirects as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        error_reply = err
        return r , request_headers , request_reply , request_text , error , error_reply
    except requests.exceptions.RequestException as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        error_reply = err
        return r , request_headers , request_reply , request_text , error , error_reply 
    error = False
    return r, request_headers, request_reply, request_text, error, error_reply 

def get(c_s,url,cua,inua):
    try:
        if c_s == ("YES"):
            if cua == ("YES"):
                headers = {'user-agent': inua}
                s = requests.Session()
                r = s.get(url , headers=headers)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"

            else:
                s = requests.Session()
                r = s.get(url)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"
        elif c_s == ("NO"):
            if cua == ("YES"):
                headers = {'user-agent': inua}
                r = requests.get(url , headers=headers)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"

            else:
                r = requests.get(url)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"
    except requests.exceptions.Timeout as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        return r , request_headers , request_reply , request_text ,error , error_reply
    except requests.exceptions.TooManyRedirects as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        error_reply = err
        return r , request_headers , request_reply , request_text , error , error_reply
    except requests.exceptions.RequestException as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        error_reply = err
        return r , request_headers , request_reply , request_text , error , error_reply 
    error = False
    return r, request_headers, request_reply, request_text, error, error_reply 

def put(c_s,url,cua,inua):
    try:
        if c_s == ("YES"):
            if cua == ("YES"):
                headers = {'user-agent': inua}
                s = requests.Session()
                r = s.put(url , headers=headers)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"

            else:
                s = requests.Session()
                r = s.put(url)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"
        elif c_s == ("NO"):
            if cua == ("YES"):
                headers = {'user-agent': inua}
                r = requests.post(url , headers=headers)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"

            else:
                r = requests.put(url)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"
    except requests.exceptions.Timeout as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        return r , request_headers , request_reply , request_text ,error , error_reply
    except requests.exceptions.TooManyRedirects as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        error_reply = err
        return r , request_headers , request_reply , request_text , error , error_reply
    except requests.exceptions.RequestException as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        error_reply = err
        return r , request_headers , request_reply , request_text , error , error_reply 
    error = False
    return r, request_headers, request_reply, request_text, error, error_reply 

def delete(c_s,url,cua,inua):
    try:
        if c_s == ("YES"):
            if cua == ("YES"):
                headers = {'user-agent': inua}
                s = requests.Session()
                r = s.delete(url , headers=headers)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"

            else:
                s = requests.Session()
                r = s.delete(url)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"
        elif c_s == ("NO"):
            if cua == ("YES"):
                headers = {'user-agent': inua}
                r = requests.delete(url , headers=headers)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"

            else:
                r = requests.delete(url)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"
    except requests.exceptions.Timeout as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        return r , request_headers , request_reply , request_text ,error , error_reply
    except requests.exceptions.TooManyRedirects as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        error_reply = err
        return r , request_headers , request_reply , request_text , error , error_reply
    except requests.exceptions.RequestException as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        error_reply = err
        return r , request_headers , request_reply , request_text , error , error_reply 
    error = False
    return r, request_headers, request_reply, request_text, error, error_reply 

def head(c_s,url,cua,inua):
    try:
        if c_s == ("YES"):
            if cua == ("YES"):
                headers = {'user-agent': inua}
                s = requests.Session()
                r = s.head(url , headers=headers)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"

            else:
                s = requests.Session()
                r = s.head(url)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"
        elif c_s == ("NO"):
            if cua == ("YES"):
                headers = {'user-agent': inua}
                r = requests.head(url , headers=headers)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"

            else:
                r = requests.head(url)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"
    except requests.exceptions.Timeout as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        return r , request_headers , request_reply , request_text ,error , error_reply
    except requests.exceptions.TooManyRedirects as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        error_reply = err
        return r , request_headers , request_reply , request_text , error , error_reply
    except requests.exceptions.RequestException as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        error_reply = err
        return r , request_headers , request_reply , request_text , error , error_reply 
    error = False
    return r, request_headers, request_reply, request_text, error, error_reply 

def option(c_s,url,cua,inua):
    try:
        if c_s == ("YES"):
            if cua == ("YES"):
                headers = {'user-agent': inua}
                s = requests.Session()
                r = s.options(url , headers=headers)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"

            else:
                s = requests.Session()
                r = s.options(url)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"
        elif c_s == ("NO"):
            if cua == ("YES"):
                headers = {'user-agent': inua}
                r = requests.options(url , headers=headers)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"

            else:
                r = requests.options(url)
                request_headers = r.request.headers
                request_reply = r.headers
                request_text = r.text
                error_reply = "Null"
    except requests.exceptions.Timeout as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        return r , request_headers , request_reply , request_text ,error , error_reply
    except requests.exceptions.TooManyRedirects as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        error_reply = err
        return r , request_headers , request_reply , request_text , error , error_reply
    except requests.exceptions.RequestException as err:
        r = ""
        error = True
        request_headers =""
        request_reply =""
        request_text =""
        error_reply = err
        return r , request_headers , request_reply , request_text , error , error_reply 
    error = False
    return r, request_headers, request_reply, request_text, error, error_reply 