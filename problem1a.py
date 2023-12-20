def dayone(input):
    d = []
    for a in input:
        a_d = ''
        for b in a:
            if b.isdigit():
                a_d += b
        d.append(int(a_d[0]+a_d[-1]))
    return sum(d)
