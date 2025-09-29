def isIP(s):
    num = s.split(".")

    if not len(num) == 4:
        return False

    for n in num:
        if n == "":
            return False
        if not (0 <= int(n) <= 255):
            return False

    return True

"""
s = input("Enter ip(ХХХ.ХХХ.ХХХ.ХХХ, где ХХХ – число от 0 до 255" )
print(isIP(s))
"""
print(isIP("123.123.2.3"))