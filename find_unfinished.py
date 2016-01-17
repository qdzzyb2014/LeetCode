#-*- coding: utf-8 -*-
import re, os
import requests
from bs4 import BeautifulSoup

from config import HEADER, COOKIE

def get_reponse():
    url = 'https://leetcode.com/problemset/algorithms/'
    cookie = COOKIE
    headers = HEADER
    print 'Geting ac problems.'
    r = requests.get(url, headers=headers)
    print 'status code: '+str(r.status_code)+'.'
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
