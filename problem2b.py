

  #2B
  def processinput2(inp):
    answlist = []
    for i in inp:
        pattern = r'Game\s+(\d+):'
        match = re.search(pattern, i)
        if match:
            vect = []
            for t in ['red','blue','green']:
                d = max(tokenparse(i,t))
                vect.append(d)
            d = int(vect[0])*int(vect[1])*int(vect[2])
            answlist.append(d)   
    return answlist

def tokenparse(text,target_word):
    pattern = rf'(\d+)\s*{re.escape(target_word)}'
    matches = re.findall(pattern, text)
    return [int(match) for match in matches]
        
        
