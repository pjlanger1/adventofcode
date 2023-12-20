import numpy as np
import pandas as pd
import re
import requests
import csv

class dataloader():
    
    def __init__(self,url):
        self.dpath = url
        self.full_input = self.loader(url)
    
    def loader(self,url):
        
        with open (url, 'r') as f:
            full_input = [column[0] for column in csv.reader(f,delimiter='\t')]
        
        return full_input
    

    
class solution():
    
    def __init__(self,full_input):
        self.input = full_input
        self.listdir = [x for x in full_input[0]]
        self.treee = full_input[1:]
        self.proctree = self.proc_tree(self.treee)
        self.sol = self.solve(self.proctree,self.listdir,'AAA','ZZZ')
        
    def proc_tree(self,tree):
        d = {}
        regex_pattern = r'.*?\((.*)\).*'
        for t in tree:
            bb = t.split("=")[0].strip()
            bb2 = re.search(regex_pattern, t).group(1).strip().split(", ")
            d[bb] = bb2
            
        return d
        
    def solve(self, proctree, listdir, start,end):
        counter = 0
        curr = start
        found = False
        
        while not found:
            for b in listdir:
                if curr == end:
                    found = True
                    return counter
                if b == 'R':
                    curr = proctree[curr][1]
                    counter += 1
                if b == 'L':
                    curr = proctree[curr][0]
                    counter += 1
                if found:
                    return counter
        return counter

