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
        self.sol = self.solve(self.proctree,self.listdir)
        
    def proc_tree(self,tree):
        d = {}
        regex_pattern = r'.*?\((.*)\).*'
        for t in tree:
            bb = t.split("=")[0].strip()
            bb2 = re.search(regex_pattern, t).group(1).strip().split(", ")
            d[bb] = bb2
            
        return d
        
    def solve(self, proctree, listdir):
        zlist = [x for x in proctree.keys() if x[-1]=='Z']
        alist = [x for x in proctree.keys() if x[-1]=='A']
        counter = 0
        curr = alist
        found = False
        
        while not found:
            for b in listdir:
                if sum([1 for c in curr if c in zlist]) == len(alist):
                    found = True
                    return counter
                if b == 'R':
                    curr = [proctree[z][1] for z in curr]
                    counter += 1
                if b == 'L':
                    curr = [proctree[z][0] for z in curr]
                    counter += 1
                if found:
                    return counter
        return counter
