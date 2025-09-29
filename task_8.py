"""
на литкоде такую же решал, так что вот...
P.S( оптимальность алгоритма оставляет желать лучшего)
"""
def isPalindrome(s):
    s = s.lower()
    for ch in s:
        if (122 < ord(ch) or ord(ch) < 97) and (48 > ord(ch) or ord(ch) > 57):
            s = s.replace(ch, "")
    stack = []
    for ch in range(len(s)//2):
        stack.append(s[ch])
    if (len(s)% 2 ):
        curr = len(s)//2 + 1
    else:
        curr = len(s)// 2
    for i in reversed(range(len(stack))):
        if stack[i] != s[curr]:
            return False
        curr += 1
    return True

str = input("Enter str: ")

print(isPalindrome(str))