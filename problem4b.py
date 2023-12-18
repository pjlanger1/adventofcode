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
        self.ptct,self.matches = self.process_data(self.data)
        self.pointrecount = self.reco(self.matches)
    
        
    def process_data(self,data):
        ptct = {}
        matches = {}
        for d in range(len(data)):
            ptc,match = self.parseline(data[d])
            ptct[d+1] = ptc
            matches[d+1] = match
        return ptct, matches
        
    def parseline(self,line):
        pointcount = 0
        matches = []
        pattern1 = r'(?<=:)\s*([\d\s]+)\s*(?=\|)'
        pattern2 = r'\|\s*(.*)'

        # Find all matches in the input string
        matches1 = [int(i) for i in re.findall(pattern1, line)[0].strip().split()]
        matches2 = [int(i) for i in re.findall(pattern2, line)[0].strip().split()]
        
        #print(matches1)
        #print(matches2)
        
        for m in matches1:
            for n in matches2:
                if m == n:
                    #matches1.remove(m)
                    #matches2.remove(n)
                    if pointcount == 0:
                        #print('match1:' + str(m) + ' ' + str(n) )
                        pointcount += 1
                    else:
                        pointcount *= 2
                    matches.append(m)
                        #print('matchagain:' + str(m) + ' ' + str(n) + ' pts;' + str(pointcount) )
                    #print(str(n) + str(m))
        return pointcount, len(matches)
    
    
    def reco(self, matches):
            accum = {key: 1 for key in range(1, len(matches.keys()) + 1)}
            for i in range(1, len(matches.keys()) + 1):
                if matches[i] > 0:
                    val = matches[i]
                    for j in range(1, val + 1):  
                        if i + j <= len(matches.keys()):
                            accum[i + j] += accum[i]

            total_scratchcards = sum(accum.values())
            return total_scratchcards



