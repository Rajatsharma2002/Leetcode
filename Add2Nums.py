l3=[]
def add2nums(l1,l2):
    for (i,j) in zip(l1,l2):
        l3.append(i+j)
        
l1=[2,3,4]
l2=[4,5,1]
add2nums(l1,l2)
print(l3)


