import random

number = random.randint(0,100)
print("Guess the number between 0 and 100"
      f"\n|{"=" * 35}|")
while True:
    n = int(input("ent num:  "))
    if n == number:
        print("CORRECT!!!")
        break
    elif n < number:
        print("Try bigger number")
    elif n > number:
        print("Trye smaller number")