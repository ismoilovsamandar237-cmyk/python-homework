# 1
name = input("enetr you name : ")
year_of_birth =int(input("enetr your year of  birth: "))
current_year = 2025
age = current_year - year_of_birth
print(f"hello {name}, you are {age }, years old" )
# 2
txt = 'LMaasleitbtui'
car_name = txt[1::2]
print(car_name)


# 3
txt = 'MsaatmiazD' 
car_name = txt[::2]
print(car_name)



# 4
txt = "I'am John. I am from London"
words = txt.split()
index = words.index("from")
recidance_area = words[index + 1]
print(recidance_area)
# 5
name = input("enter words or sentence:  ")
reversed_text = name [::-1]
print("reverse text : " , reversed_text)

# 6
text = input("Enter a word or sentence: ")  
vowels = "aeiouAEIOU"                      
count = 0                                  

for char in text:                           
    if char in vowels:                      
        count += 1                          
print("Number of vowels:", count)           

#7
numbers = [12, 45, 7, 89, 23]  
maximum = max(numbers)          
print("Maximum value is:", maximum)

# 8
word = input("Enter a word: ")
if word == word[::-1]:                     
    print("It is a palindrome")
else:
    print("It is not a palindrome")


# 9
email = input("Enter your email: ")
domain = email.split("@")[1]      
print("Email domain:", domain)

# 10
import random
import string


characters = string.ascii_letters + string.digits + string.punctuation


password = ''.join(random.choice(characters) for i in range(12))

print("Generated password:", password)

