def paren(s):
    open=['[','(','{']
    close=[']',')','}']

    l=[]
    for i in s:
        if i in open:
            l.append(i)
        elif i in close:
            value=close.index(i)
            if len(l)>0 and open[value]==l[len(l)-1]:
                l.pop()
            else:
                return False

    if len(l)==0:
        return True
    else:
        return False

if __name__ == '__main__':
    s='{[}'
    Result=paren(s)
    print(Result)
