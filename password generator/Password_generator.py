import random
letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
         'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','-','_',',','.','/','<','>','?',';',':','{','[','}',']']
print("Welcome to password generator! ")
n_letters=int(input("How many letters you want in password?\n"))
n_symbols=int(input("How many symbols you want in password?\n"))
n_numbers=int(input("How many numbers you want in password?\n"))
password_list=[]
for i in range(n_letters):
    x=random.choice(letters)
    password_list+=x
# print(password)
for i in range(n_symbols):
    x=random.choice(symbols)
    password_list+=x
for i in range(n_numbers):
    x=random.choice(numbers)
    password_list+=x
random.shuffle(password_list)
# print(password_list)
password=""
for i in password_list:
    password+=i
print(f"Your password is '{password}'")