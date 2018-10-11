from urllib import request
from urllib import parse
from urllib.parse import quote

from bs4 import BeautifulSoup

class Search(object):
    URL_SEARCH  = 'http://search.zongheng.com/s?keyword=%s'

    def __init__(self):
        pass

    def search(self,keyword):
        url = self.URL_SEARCH % quote(keyword)
        search_content = ''
        with request.urlopen(url) as search:
            search_content = search.read().decode('utf-8')
        
        print(search_content)


s = Search()
s.search('雪中悍刀行')

