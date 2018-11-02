from bs4 import BeautifulSoup
import requests

def findhref(url):
    try:
        r = requests.get(url)
        html = r.content
        soup = BeautifulSoup(html)
        data = ""
        for a in soup.find_all('a', href=True):
            data = data+str( a['href']+ "\n")
    except requests.exceptions.Timeout as err:
        data = "error"
    except requests.exceptions.TooManyRedirects as err:
        data = "error"
    except requests.exceptions.RequestException as err:
        data = "error"
    
    return data