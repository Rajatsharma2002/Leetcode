def romint(s):
    dict = {'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}

    result=0
    for i in range(len(s)):
        a=dict[s[i]]
        b=dict[s[i-1]]
        if i>0 and a>b:
            result+=a-2*b
        else:
            result+=a
    return result
    # roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    #     counter = 0
    #     for i in range(0, len(s) - 1):
    #         if roman[s[i]] < roman[s[i+1]]:
    #             counter -= roman[s[i]]
    #         else:
    #             counter += roman[s[i]]
    #     return counter + roman[s[-1]]

if __name__ == '__main__':
    x='LVIII'
    Result=romint(x)
    print(Result)




