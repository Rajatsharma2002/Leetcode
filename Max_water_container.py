def maxwater(x):
    i=0
    j=len(x)-1
    maxval=0
    while i<j:
        maxval = max(maxval,(j-i)*min(x[i],x[j]))

        if x[i]<x[j]:
            i=i+1
        else:
            j=j-1
    return maxval

if __name__ == '__main__':
    x=[1,8,6,2,5,4,8,3,7]
    Result=maxwater(x)
    print(f"Maximum water that can be contained in container : {Result}")

