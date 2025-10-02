"""
на литкоде такую же решал, тут можно несколько слов вносить типо "a,,.//[][a" и т.д
P.S( оптимальность алгоритма оставляет желать лучшего)
"""
def isPalindrome(s):
    s = s.lower()
    for ch in s:
        if (122 < ord(ch) or ord(ch) < 97) and (48 > ord(ch) or ord(ch) > 57):
            s = s.replace(ch,"")
    print(s)
    if(s == s[::-1]): print(True)
    else:print(False)

str = input("Enter str: ")
isPalindrome(str)