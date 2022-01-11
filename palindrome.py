def palidrome(x):
    x=str(x)
    rev=x[::-1]
    if x[0]=='-':
        return False
    elif x==rev:
        return True
    else:
        return False

if __name__ == '__main__':
    x=int(input())
    Result=palidrome(x)
    print(f'The given input is Palindrome (True/False) : {Result}')