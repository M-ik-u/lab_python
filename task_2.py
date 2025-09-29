to_del ="aeiou"

l = input("Enter string: ")
new_l =""

for i in l:
    if i not in to_del:
        new_l += i

print(f"Result: {new_l}")
