from bs4 import BeautifulSoup
import requests

def findhref(url):
    try:
        r = requests.get(url)
        html = r.content
        soup = BeautifulSoup(html)
        data = ""
        href = []
        for a in soup.find_all('a', href=True):
            data = data+str( a['href']+ "\n")
        data=data.splitlines()
        href.extend(data)

    except requests.exceptions.Timeout as err:
        data = err
    except requests.exceptions.TooManyRedirects as err:
        data = err
    except requests.exceptions.RequestException as err:
        data = err
    
    return data