import re
from urllib import request

import bs4
from bs4 import BeautifulSoup

root_url = 'http://book.zongheng.com/store/'

class HtmlSpider(object):

    def __init__(self):
        pass

    def get_html_body(self, url):
        home_webpage_content = ''
        with request.urlopen(url) as home_webpage:
            home_webpage_content = home_webpage.read().decode('utf-8')
        home_soup = BeautifulSoup(home_webpage_content,"lxml")
        return home_soup.body
 

class Category(HtmlSpider):

    def __init__(self):
        pass

    def get_category(self):
        url_home = 'http://www.zongheng.com/'
        category = {}
        body = self.get_html_body(url_home)
        ul_classify = body.find('div',class_="tabA-float cate-cell").find('ul')
        li_list = ul_classify.find_all('li')

        for li in li_list:
            category[li.a.string] = li.a.get('href')

        return category

class Store(HtmlSpider):
    store_url = 'http://book.zongheng.com/store.html'

    def __init__(self,store_url=store_url):
        self.store_url = store_url
    
    def get_category(self):
        body = self.get_html_body(self.store_url)
        categories = body.find('div',class_='nr br sub').find_all('a',class_='store')
        category = {}
        for a_tag in categories:
            category[a_tag.attrs['categoryid']]= a_tag.contents[0]  

        return category 

    def get_subcategory(self,category_id):
        subcategory_url = 'http://book.zongheng.com/store/c%s/c0/b0/u0/p1/v9/s9/t0/u0/i1/ALL.html' % category_id
        subcategories = self.get_html_body(subcategory_url).find('div',class_='sublevel').find_all('a',class_='store')
        subcategory= {}
        for a_tag in subcategories:
            subcategory[a_tag.attrs['childcategoryid']] = a_tag.contents[0]

        return subcategory
        
    def get_book_list(self, category_id, subcategory_id, page, **kw):
        '''http://book.zongheng.com/store/c1/c1008/b0/u0/p1/v9/s9/t0/u0/i1/ALL.html'''
        '''http://book.zongheng.com/store/c父分类id/c子分类id/b书记类型(男0，女1)/u排序类型/p页码/v收费类型/s是否连载/t文字多少/u更新时间/i是否图文混排(混1，否2)/根据首字母排序(ALL/A/B/C).html'''

        book_list_url = 'http://book.zongheng.com/store/c%s/c%s/b0/u0/p1/v9/s9/t0/u0/i1/ALL.html' % (category_id, subcategory_id)
        
        ''' name, author, category, serial_status, intro, last_update_time, bookupdate, book_url, img_url '''
        book_list = []
        books_div = self.get_html_body(book_list_url).find('div',class_='store_collist').find_all('div',class_='bookbox')
        for book_tags in books_div:
            book = {}
            a_tag = book_tags.find('div',class_='bookimg').a
            book_url = a_tag.get('href')
            book['book_url'] = book_url
            book_id = re.findall(r'\d+',book_url)[0]

            book_img = a_tag.find('img').get('src')
            book['book_img'] = book_img

            bookinfo_div = book_tags.find('div',class_='bookinfo')
            book_name = bookinfo_div.find('div','bookname').a.string
            book['book_name'] = book_name

            bookilnk = bookinfo_div.find('div',class_='bookilnk')

            book_author = bookilnk.find_all('a')[0].string
            book['book_author'] = book_author
            book_category = bookilnk.find_all('a')[1].string
            book['book_category'] = book_category

            serial_status = bookilnk.find_all('span')[0].string.strip()
            book['serial_status'] = serial_status
            last_update_time = bookilnk.find_all('span')[1].string.strip()
            book['last_update_time'] = last_update_time

            book_intro = bookinfo_div.find('div',class_='bookintro').string
            book['book_intro'] = book_intro
            latest_chapter = bookinfo_div.find('div',class_='bookupdate').a.string
            book['latest_chapter'] = latest_chapter
        

            book_list.append(book)
        return book_list

    def get_book_directory(self,book_id):
        '''http://book.zongheng.com/showchapter/753363.html'''

        chapter_url = 'http://book.zongheng.com/showchapter/%s.html' % book_id
        volume_list_divs = self.get_html_body(chapter_url).find("div",class_='volume-list').children

        volume_dict = {}
        for volume_div in volume_list_divs:
            if isinstance(volume_div,bs4.element.Tag):
                volume_title = volume_div.find('div',class_='volume').find('em',class_='v-line').next_element
                print('卷标题:',volume_title)
                volume_li = volume_div.find('ul',class_='chapter-list').find_all('li')

                chapter_list = []           
                for li in volume_li:
                    chapter_dict = {}
                    chapter_title = li.a.string
                    chapter_url = li.a.get('href')
                    chapter_dict['chapter_title'] = chapter_title
                    chapter_dict['chapter_url'] = chapter_url
                    chapter_list.append(chapter_dict)

                volume_dict[volume_title] = chapter_list

        return volume_dict

class Novel(HtmlSpider):

    ''' catalogue , pre_chapter ,next_chapter '''

    def __init__(self):
        pass

    def get_chapter_info(self,novel_id,chapter_id):
        novel_url = 'http://book.zongheng.com/chapter/%s/%s.html' % (novel_id,chapter_id)

        body = self.get_html_body(novel_url)

        acticle = {}
        navigations = body.find('div',class_='chap_btnbox').find_all('a')
        acticle['catalogue_url'] = navigations[0].get('href')
        acticle['pre_chapter'] = ''  if 'http' not in navigations[1].get('href') else navigations[1].get('href')
        acticle['next_chapter'] = navigations[2].get('href')
        
        acticle_paragraphs = []
        acticle_body = body.find(itemprop="acticleBody")
        paragraphs = acticle_body.find_all('p')
        for paragraph in paragraphs:
            p = paragraph.string.strip() 
            if p != '':
                acticle_paragraphs.append(p)

        acticle['paragraphs'] = acticle_paragraphs
        return acticle


'''http://book.zongheng.com/chapter/753363/41640403.html'''
'''http://book.zongheng.com/chapter/753363/41639623.html '''

novel = Novel()
novel = novel.get_chapter_info('753363','41640403')

print(novel)