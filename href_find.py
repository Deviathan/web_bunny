from bs4 import BeautifulSoup
import requests

def findhref(url):
    if url.startswith('http://') or url.startswith('https://'):
        url = url
    else:
        prefix = 'http://'
        url = prefix + url   
    try:
        r = requests.get(url)
        html = r.content
        soup = BeautifulSoup(html)
        data = ""
        href = []
        for a in soup.find_all('a', href=True):
            data = data+str( a['href']+ "\n")
        href.extend(data)
    except requests.exceptions.Timeout as err:
        data = err
    except requests.exceptions.TooManyRedirects as err:
        data = err
    except requests.exceptions.RequestException as err:
        data = err
    
    return data