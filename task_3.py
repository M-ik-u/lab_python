password = input("Enter password: ")

if len(password) < 16:
    print("Too short")
elif password.isalpha() or password.isdigit():
    print("weak pass")
else:
    print("strong pass")