import requests

def http_requests(c_s,request_type,url,cua,inua):
    global r, error
    error = False
    request_headers , request_reply , request_text, r , request_encoding = "", "", "", "", ""
    
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
                else:
                    s = requests.Session()
                    r = s.post(url)
            elif c_s == ("NO"):
                if cua == ("YES"):
                    headers = {'user-agent': inua}
                    r = requests.post(url , headers=headers)
                else:
                    r = requests.post(url)  
            request_headers,request_reply,request_text,request_encoding=output(r)
        except requests.exceptions.Timeout as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = "","","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        except requests.exceptions.TooManyRedirects as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = "","","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        except requests.exceptions.RequestException as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = "","","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        error = False
        return r , request_headers , request_reply , request_text , request_encoding, error


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
                else:
                    s = requests.Session()
                    r = s.get(url)
            elif c_s == ("NO"):
                if cua == ("YES"):
                    headers = {'user-agent': inua}
                    r = requests.get(url , headers=headers)
                else:
                    r = requests.get(url)
            request_headers,request_reply,request_text,request_encoding=output(r)
        except requests.exceptions.Timeout as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = "","","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        except requests.exceptions.TooManyRedirects as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = "","","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        except requests.exceptions.RequestException as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = "","","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        error = False
        return r , request_headers , request_reply , request_text , request_encoding, error

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
                else:
                    s = requests.Session()
                    r = s.put(url)
            elif c_s == ("NO"):
                if cua == ("YES"):
                    headers = {'user-agent': inua}
                    r = requests.post(url , headers=headers)
                else:
                    r = requests.put(url)
            request_headers,request_reply,request_text,request_encoding=output(r)
        except requests.exceptions.Timeout as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = err,"","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        except requests.exceptions.TooManyRedirects as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = err,"","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        except requests.exceptions.RequestException as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = err,"","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        error = False
        return r , request_headers , request_reply , request_text , request_encoding, error 


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

                else:
                    s = requests.Session()
                    r = s.delete(url)
            elif c_s == ("NO"):
                if cua == ("YES"):
                    headers = {'user-agent': inua}
                    r = requests.delete(url , headers=headers)
                else:
                    r = requests.delete(url)
            request_headers,request_reply,request_text,request_encoding=output(r)
        except requests.exceptions.Timeout as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = err,"","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        except requests.exceptions.TooManyRedirects as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = err,"","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        except requests.exceptions.RequestException as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = err,"","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        error = False
        return r , request_headers , request_reply , request_text , request_encoding, error 


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
                else:
                    s = requests.Session()
                    r = s.head(url)
            elif c_s == ("NO"):
                if cua == ("YES"):
                    headers = {'user-agent': inua}
                    r = requests.head(url , headers=headers)
                else:
                    r = requests.head(url)
            request_headers,request_reply,request_text,request_encoding=output(r)
        except requests.exceptions.Timeout as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = err,"","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        except requests.exceptions.TooManyRedirects as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = err,"","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        except requests.exceptions.RequestException as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = err,"","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        error = False
        return r , request_headers , request_reply , request_text , request_encoding, error 


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

                else:
                    s = requests.Session()
                    r = s.options(url)
            elif c_s == ("NO"):
                if cua == ("YES"):
                    headers = {'user-agent': inua}
                else:
                    r = requests.options(url)
            request_headers,request_reply,request_text,request_encoding=output(r)
        except requests.exceptions.Timeout as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = err,"","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        except requests.exceptions.TooManyRedirects as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = err,"","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        except requests.exceptions.RequestException as err:
            error = True
            r,request_headers, request_reply,request_text,request_encoding = err,"","","",""
            return r , request_headers , request_reply , request_text , request_encoding, error
        error = False
        return r , request_headers , request_reply , request_text , request_encoding, error 
        
def output(r):
    request_headers = r.request.headers
    request_reply = r.headers
    request_text = r.text
    request_encoding = r.encoding
    return request_headers,request_reply,request_text,request_encoding