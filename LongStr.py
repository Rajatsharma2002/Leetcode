def lengthOfLongestSubstring(s):
    str=''
    maxlen=0
    for value in s:
        # if value not present in str then we will add that value and move forward
        if value not in str:
            str=str+value
        # if value is present in str then we have to delete the index of the repeting element
        # from str and update the value in str
        else:
            str=str[str.index(value)+1:]+value
        # checking maximum value between current and previous and update with new value
        maxlen = max(maxlen, len(str))
    return maxlen,str

if __name__ == '__main__':
    s='aklsbabcdefgh'
    result=lengthOfLongestSubstring(s)
    print(f"Length of Maximum Possible Non Repeating Substring : {result}")
