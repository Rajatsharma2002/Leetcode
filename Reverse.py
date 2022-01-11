# def reverse(x):
#     rev=0
#     num=x
#     num = str(num)
#     while(x!=0):
#         rev=rev*10+x%10
#         x=x//10
#     if rev>pow(2,31):
#         return 0
#
#     elif num[0] == '-':
#         symbol = num[0]
#         reverse = num[::-1]
#         return f'{symbol + reverse[:len(num) - 1]}'
#
#     else:
#         return rev
#
# if __name__ == '__main__':
#     x=123
#     Result=reverse(x)
#     print(f"Reversed Number : {Result}")

def reverse(x):

    x = str(x)
    reverse = x[::-1]
    rev = int(reverse[:len(x) - 1])

    if rev > pow(2, 31):
        return 0

    elif x[0] == '-':
        symbol = x[0]
        return symbol + reverse[:len(x) - 1]

    elif x[len(x) - 1] == '0':
        r = int(reverse)
        return r

    else:
        return reverse


if __name__ == '__main__':
    x = -12876
    Result = reverse(x)
    print(f"Reversed Number : {Result}")





