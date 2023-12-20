def parttwo(input):
    d = []
    for a in input:
        staging = []
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
