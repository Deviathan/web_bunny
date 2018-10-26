import requests


def post(url,cua,inua):
    try:
        r = requests.post(url)
        result = r.text   
        r.raise_for_status()
    except requests.exceptions.Timeout as err:
        r = err
        error = True
        return r,error
    except requests.exceptions.TooManyRedirects as err:
        r = err
        error = True
        return r,error
    except requests.exceptions.RequestException as err:
        r = err
        error = True
        return r,error
    error = False
    return r,result,error