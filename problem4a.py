import numpy as np
import pandas as pd
import csv
import os
import re

class dataloader():
    
    def __init__(self,url):
        self.dpath = url
        self.full_input = self.loader(url)
    
    def loader(self,url):
        
        with open (url, 'r') as f:
            full_input = [column[0] for column in csv.reader(f,delimiter='\t')]
        
        return full_input

class solution():
    
    def __init__(self,data):
        self.data = data.full_input
        self.ptct = self.process_data(self.data)
    
        
    def process_data(self,data):
        ptct = 0
        for d in data:
            ptct += self.parseline(d)
        return ptct
        
    def parseline(self,line):
        pointcount = 0
        matches = []
        pattern1 = r'(?<=:)\s*([\d\s]+)\s*(?=\|)'
        pattern2 = r'\|\s*(.*)'

        # Find all matches in the input string
        matches1 = [int(i) for i in re.findall(pattern1, line)[0].strip().split()]
        matches2 = [int(i) for i in re.findall(pattern2, line)[0].strip().split()]
        
        print(matches1)
        print(matches2)
        
        for m in matches1:
            for n in matches2:
                if m == n:
                    #matches1.remove(m)
                    #matches2.remove(n)
                    if pointcount == 0:
                        print('match1:' + str(m) + ' ' + str(n) )
                        pointcount += 1
                    else:
                        pointcount *= 2
                        print('matchagain:' + str(m) + ' ' + str(n) + ' pts;' + str(pointcount) )
                    #print(str(n) + str(m))
        return pointcount
        
