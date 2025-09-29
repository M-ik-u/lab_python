numb = int(input("Enter num "))

if not numb %7:
    print("Magic number")
else:
    numb = str(numb)
    sum = 0
    for i in numb:
        sum += int(i)
    print(f"Result: {sum}")