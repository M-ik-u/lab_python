def isPalindrome():
    s = input("enter a string: ")
    s = s.lower()
    for ch in s:
        if (122 < ord(ch) or ord(ch) < 97) and (48 > ord(ch) or ord(ch) > 57):
            s = s.replace(ch, "")
    if (s == s[::-1]): print("palindrome")
    else : print("not palindrome")

def beginningwithAonly():
    line = input("enter words: ")

    for i in line.split():
        if i[0] == "A":
            print(i)
        else:
            continue

def dictionary(n):
    dict = {}
    for i in range(1, n + 1):
        dict[i] = len([x for x in range(1, i + 1) if i % x == 0])
    return dict

def nechet(n):
    list = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            list.append(i)
    print(list)

def minindex():
    list = []
    line = input("enter numbers: ")
    for i in line.split():
        list.append(int(i))
    print(f"min value = {min(list)}, index = {list.index(min(list))}")

def sorttuple(n):
    tupple = ()
    for part in n.split():
        tupple = tupple + (part, )
    tupple = list(tupple)
    tupple = sorted(tupple,key=len, reverse=True)
    return tuple(tupple)

def countsa(s):
    n = s.count("a")
    return n

def nodoubles(s):
    sset = []
    for num in s.split():
        sset.append(int(num))
    return set(sset)

def peresechsets(s1,s2):
    ss1 = []
    for num in s1.split():
        ss1.append(int(num))
    ss1 = set(ss1)

    ss2 = []
    for num in s2.split():
        ss2.append(int(num))
    ss2 = set(ss2)

    return ss1 & ss2

def squareofnumbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum

if __name__ == "__main__":
    #1 isPalindrome()
    #2 beginningwithAonly()
    #3 print(dictionary(int(input("enter n: "))))
    #4 nechet(int(input("enter n: ")))
    #5 minindex()
    #6 print(sorttuple(input("enter words: ")))
    #7 print(countsa(input("enter string: ")))
    #8 print(nodoubles(input("enter numbers: ")))
    #9 print(peresechsets(input("enter s1: "), input("enter s2: ")))
    #10 print(squareofnumbers(int(input("enter n: "))))





