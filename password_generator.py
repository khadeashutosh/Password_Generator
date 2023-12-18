import random
symbols=['@','#','$','%','^','&','*','!']

small_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

capital_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers=['0','1','2','3','4','5','6','7','8','9',]
print("Welcome to the Password Generator \n")

n_symbols=int(input("Enter many symbols you want to in your password \n"))
n_small_letters=int(input("How many small letters you want in your password \n"))
n_capital_letters=int(input("How many capital letters you want in your password \n"))
n_numbers=int(input("How many numbers you want in your password \n"))
password=""
for result in range(1,n_symbols+1):
    sym=random.choice(symbols)
    password=password +sym    
print(password) 
for rsult in range(1,n_small_letters+1):
    small=random.choice 
   