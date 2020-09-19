from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

if __name__ == '__main__':
    try:
        html = urlopen('http://www.pythonscraping.com/pages/page1.html')
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    else:
        bs = BeautifulSoup(html, 'lxml')
        print(bs.h1)
