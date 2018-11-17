import requests

def http_requests(c_s,request_type,url,cua,inua):
    global r, error, result, error_reply 
    error = False
    request_headers , request_reply , request_text, error_reply , r , result = "", "", "", "", "" , ""
    
    #checks the url if http:// or https:// is inserted 
    if url.startswith('http://') or url.startswith('https://'):
        url = url
    #if its not it adds http:// to the prefix of the url 
    else:
        prefix = 'http://' 
        url = prefix + url

    #POST REQUEST
    if request_type == "POST":
        try:
            #SESSION
            if c_s == ("YES"):
                #USER AGENT
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
        error = False
        return r, request_headers, request_reply, request_text, error, error_reply 

    #GET REQUEST
    if request_type == "GET":
        try:
            #SESSION
            if c_s == ("YES"):
                #USER AGENT
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

    #PUT REQUEST
    if request_type == "PUT":
        try:
            #SESSION
            if c_s == ("YES"):
                #USER AGENT
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

    #DELETE REQUEST
    if request_type == "DELETE":
        try:
            #SESSION
            if c_s == ("YES"):
                #USER AGENT
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


    #HEAD REQUEST
    if request_type == "HEAD":
        try:
            #SESSION
            if c_s == ("YES"):
                #USER AGENT
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


    #OPTIONS REQUEST
    if request_type == "OPTIONS":
        try:
            #SESSION
            if c_s == ("YES"):
                #USER AGENT
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
        