import queue
import requests
from bs4 import BeautifulSoup
from threading import  Thread

class Bole:
    def __init__(self):
        self.index_task = queue.Queue()
        self.start_url = 'http://python.jobbole.com/all-posts/'
        self.index_task.put(self.start_url)
        self.index_num = 0
        self.index_history = []
        self.detail_num = 0
        self.detail_task = queue.Queue()
        self.detail_history = []

    def get_index_html(self,url):
        """
        request 爬取index页面
        :return:
        """
        if url not in self.index_history:
            self.index_history.append(url)
            html = requests.get(url).text
            # self.log(html)
            print('爬取{}index页面'.format(self.count()))
            print('剩余{}个index页面'.format(self.index_task.qsize()))
            # self.log_index()
            return html

    def get_detail_html(self,url):
        """
        request 爬取detail页面
        :return:
        """
        if url not in self.detail_history:
            self.detail_history.append(url)
            html = requests.get(url).text
            print('爬取{}detail页面'.format(self.count_detail()))
            print('剩余{}个detail页面'.format(self.detail_task.qsize()))
            # self.log_detail()
            return html


    def parse_html(self,html):
        """
        解析index 页面，获取下一页index页面url,并添加到index_task中
        :return:
        """
        parse_html = BeautifulSoup(html)
        #找到下一页的a标签
        a_list = parse_html.find_all('a',class_='next page-numbers')
        #在a标签中找到url，并添加到index_task中
        for a in a_list:
            next_url = a.attrs.get('href')
            self.index_task.put(next_url)

        """
        解析detail页面，获取每一篇文章的url,并添加到detail_task中
    
        """
        #找到所有文章的a标签
        article_list = parse_html.find_all('a',class_='archive-title')
        #在a标签中找到每个文章的url，并添加到detail_task中
        for article in article_list:
            article_url = article.attrs.get('href')
            self.detail_task.put(article_url)

    def get_inedx_url(self):
        """
        从index_task取到url开始爬取
        :return:
        """
        while True:
            url = self.index_task.get()
            html = self.get_index_html(url)
            self.parse_html(html)


    def get_detail_url(self):
        """
        从detail_task取到url开始爬取文章页
        :return:
        """
        while True:
            url = self.detail_task.get()
            # html = self.get_detail_html(url)
            Thread(target=self.get_detail_html,args=(url,)).start()



    def start(self):
        """
        开始运行爬取页面
        :return:
        """

        t1 = Thread(target=self.get_inedx_url)
        t2 = Thread(target=self.get_detail_url)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    def log(self,html):
        """
        打印爬取的页面html
        :return:
        """
        print(html)

    def log_index(self):
        """
        打印爬取了哪些index页面
        :return:
        """
        print('爬取的index页面列表{}'.format(self.index_history))

    def log_detail(self):
        """
        打印爬取了哪些detail页面
        :return:
        """
        print('爬取的detail页面列表{}'.format(self.detail_history))

    def count(self):
        """
        爬取index页面计数
        :return:
        """
        self.index_num +=1
        return self.index_num

    def count_detail(self):
        """
        爬取detail页面计数
        :return:
        """
        self.detail_num += 1
        return self.detail_num

if __name__=='__main__':
    page = Bole()
    page.start()





