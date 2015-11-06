#-*- coding: utf-8 -*-
import os, re
import requests
from bs4 import BeautifulSoup


class Problem(object):
    def __init__(self, problem_type):
        self.problem_type = problem_type
        self.url = 'https://leetcode.com/problemset/'+problem_type+'/'
        # self.problems = self.collect()
        self.cookie = '_ga=GA1.2.318572932.1444183786; csrftoken=k9icuHvRoq72kOzOP5rDkHaFV4bXnBln; PHPSESSID=9a9xsoscuaz3o5x1yq6bh6q95g6ajq00; __atuvc=23%7C40%2C63%7C41%2C42%7C42%2C18%7C43; _gat=1'
        self.headers = {
        'Host': 'leetcode.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': self.cookie,
        'Connection': 'keep-alive',
        'Cache-Contro': 'max-age=0'
        }
        self.r = requests.get(self.url, headers=self.headers)
        if 'qdzzyb2014' not in self.r.text:
            raise Exception('log in Failure. Please change cookies')
        self.basedir = os.path.abspath(os.path.dirname(__file__))
        # self.unreview = self.main()


    def _find_done(self):
        soup = BeautifulSoup(self.r.text, 'html.parser')
        aclist = []
        for i in soup.find_all(class_='ac'):
            for parent in i.parents:
                if parent.name == 'tr':
                    aclist.append(parent)
        return aclist

    def aclist_to_dic(self):
        def parser(html):
            useful_info = html.contents[1::2]
            index = useful_info[1].string
            name = useful_info[2].a.string.replace(' ', '')
            return {index: name}
        
        tmp = map(parser, self._find_done())
        res = {}
        for i in tmp:
            res.update(i)
        return res

    def finished_list(self):
        filename = 'README.md'
        res = []
        with open(os.path.join(self.basedir, filename), 'r') as f:
            for i in f:
                match = re.search(r'[0-9]+', i)
                if match:
                    res.append(int(match.group(0)))
        return res

    def mk_dir(self):
        ac = self.aclist_to_dic()
        finished = self.finished_list()
        for i in ac:
            if i not in finished:
                path = os.path.join(self.basedir+'\\algorithms', ac[i])
                if not os.path.exists(path):
                    os.mkdir(path)
                    open(os.path.join(path, ac[i]+'.py'), 'w')
                    print path
                    
    def unfinished_list(self):
        ac = self.aclist_to_dic()
        finished = self.finished_list()
        print len(ac)
        print len(finished)
        return [i for i in ac if i not in finished]

    

p = Problem('algorithms')
print p.unfinished_list()
        
