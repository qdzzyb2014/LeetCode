#-*- coding: utf-8 -*-
import os, re
import requests
from bs4 import BeautifulSoup

from config import HEADER, COOKIE

class Problem(object):
    def __init__(self, problem_type):
        self.problem_type = problem_type
        self.url = 'https://leetcode.com/problemset/'+problem_type+'/'
        # self.problems = self.collect()
        self.cookie = COOKIE
        self.headers = HEADER
        self.r = requests.get(self.url, headers=self.headers)
        if 'qdzzyb2014' not in self.r.text:
            raise Exception('log in Failure. Please change cookies')
        self.basedir = os.path.abspath(os.path.dirname(__file__))
        # self.unreview = self.main()


    def _find_done(self):
        def find_tr_tag(self, i):
            for parent in i.parents:
                if parent.name == 'tr':
                    return parent

        soup = BeautifulSoup(self.r.text, 'html.parser')
        aclist = []
        return map(find_tr_tag, soup.find_all(class_='ac'))
        '''
        for i in soup.find_all(class_='ac'):
            for parent in i.parents:
                if parent.name == 'tr':
                    aclist.append(parent)
        return aclist
        '''

    def aclist_to_dic(self):
        def parser(html):
            useful_info = html.contents[1::2]
            index = useful_info[1].string
            name = useful_info[2].a.string.replace(' ', '')
            return {int(index): name}
        
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
        return [i for i in ac.keys() if i not in finished]

    

p = Problem('algorithms')
p.mk_dir()
print sorted(p.unfinished_list())
        
