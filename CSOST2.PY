
#TASK-3 PASSWORD GENERATOR

import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','_','+']
print("WELCOME TO PASSWORD GENERATOR")
d_letters=int(input("Enter number of letters needed in your password:"))
d_numbers=int(input("Enter count of numbers in your password:"))
d_symbols=int(input("Enter count of symbols in your password:"))
password=""
for i in range(1,d_letters+1):
    char=random.choice(letters)
    password+=char
for i in range(1,d_symbols+1):
    char=random.choice(symbols)
    password+=char
for i in range(1,d_numbers+1):
    char=random.choice(numbers)
    password+=char
print(password)









    
    

