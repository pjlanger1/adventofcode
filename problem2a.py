#2A

def processinput(r,g,b,inp):
    validlist = []
    for i in inp:
        pattern = r'Game\s+(\d+):'
        match = re.search(pattern, i)
        if match:
            print(i)
            flag = True
            #match.group(1)
            for t in ['red','blue','green']:
                d = max(tokenparse(i,t))
                #print(t+" "+str(d)+" "+str(r))
                #print(t+" "+str(d)+" "+str(b))
                #print(t+" "+str(d)+" "+str(g))
                if t == 'red':
                    if d > r:
                        flag = False
                        break
                if t == 'blue':
                    if d > b:
                        flag = False
                        break
                if t == 'green':
                    if d > g:
                        flag = False
                        break
            if flag:
                validlist.append(int(match.group(1)))
    return validlist

def tokenparse(text,target_word):
    pattern = rf'(\d+)\s*{re.escape(target_word)}'
    matches = re.findall(pattern, text)
    return [int(match) for match in matches]
