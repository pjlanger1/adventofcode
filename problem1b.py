
diction = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

def parttwo(input):
    d = []
    #for each line in input string
    for a in input:
        #staging takes a list of parsed digits/written numbers in numeric
        staging = []
        #this is for building strings for comparison with the dictionary
        stagestr = ''
        for b in a:
            if b.isdigit():
                staging.append(str(b))
                if stagestr != '':
                    stagestr = ''
            else:
                stagestr += b
                for k in diction.keys():
                    if k in stagestr:
                        staging.append(str(diction[k]))
                        stagestr = '' + stagestr[-1]
        d.append(staging[0]+staging[-1])
    return d
