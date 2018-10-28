import requests


def put(url,cua,inua):
    try:
        if cua == ("YES"):
            headers = {'user-agent': inua}
            r = requests.put(url , headers=headers)
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
        #r.raise_for_status()
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