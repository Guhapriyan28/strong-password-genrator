import random

#create list for letters,numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator♥")

no_let =int(input("enter how many numbers of letter should in password:\n"))
no_nu = int(input("enter how many numbers  should in password:\n"))
no_sy =int(input("enter how many numbers of symbols should in password:\n"))
#choice letters , number and symbols random
password_list =[]

for i in range(1,no_let+1):
    password_list.append(random.choice(letters))
for i in range(1,no_nu+1):
    password_list.append(random.choice(numbers))
for i in range (1,no_sy+1):
    password_list.append(random.choice(symbols))
    random.shuffle(password_list)
#covert list to string>
password=""

for i in password_list:
    password+=i


print(f"your strong password is :{password}")