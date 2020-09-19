from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

if __name__ == '__main__':
    try:
        html = urlopen('http://www.pthonscraping.com/pages/page1.html')
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found.")
    else:
        bs = BeautifulSoup(html, 'lxml')
        print(bs.h1)
