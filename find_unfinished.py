#-*- coding: utf-8 -*-
import re, os
import requests
from bs4 import BeautifulSoup

def get_reponse():
    url = 'https://leetcode.com/problemset/algorithms/'
    cookie = '_ga=GA1.2.318572932.1444183786; csrftoken=k9icuHvRoq72kOzOP5rDkHaFV4bXnBln; PHPSESSID=9a9xsoscuaz3o5x1yq6bh6q95g6ajq00; __atuvc=23%7C40%2C63%7C41%2C42%7C42%2C18%7C43; _gat=1'
    headers = {
    'Host': 'leetcode.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': cookie,
    'Connection': 'keep-alive',
    'Cache-Contro': 'max-age=0'
    }

    r = requests.get(url, headers=headers)
    return r.text

def find_done(text):
    soup = BeautifulSoup(text, 'html.parser')
    #print soup.prettify()
    aclist = soup.find_all(class_='ac')
    res = []
    for i in aclist:
        for parent in i.parents:
            if parent.name == 'td':
                res.append(int(parent.next_sibling.next_sibling.string))
    return res

def finished_list():
    basedir = os.path.abspath(os.path.dirname(__file__))
    filename = 'README.md'
    res = []
    with open(os.path.join(basedir, filename), 'r') as f:
        for i in f:
            match = re.search(r'[0-9]+', i)
            if match:
                res.append(int(match.group(0)))
    return res

def main():
    ac = find_done(get_reponse())
    marked = finished_list()
    res = [i for i in ac if i not in marked]
    # print res
    return res

if __name__ == '__main__':
    res = main()
    print res
