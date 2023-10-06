import random

print("0 for rock, 1 for paper and 2 for scissor.")
user = int(input("Enter your choice. "))
com = random.randint(0, 2)
print(f"Computer choice is {com}")
if user == 0 and com == 1:
    print("you lose")
elif user == 0 and com == 2:
    print("you win")
elif user == 1 and com == 0:
    print("you win")
elif user == 1 and com == 2:
    print("you lose")
elif user == 2 and com == 0:
    print("you lose")
elif user == 2 and com == 1:
    print("you win")
else:
    print("It's a draw.")
