def medianofarray(x,y):
    for i in y:
        x.append(i)

    x.sort()
    print(x)

    l = len(x) // 2
    if len(x)%2==0:
        median=(x[l-1]+x[l])/2

    else:
        median=x[l]
    return median


if __name__ == '__main__':
    x=[900]
    y=[5,8,10,20]
    Result=medianofarray(x,y)
    print(f"Median is : {Result}")

