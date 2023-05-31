# 1.	Write a Python program to add two numbers.
a=1
b=4
c=a+b
print(c)

# 2.	Write a Python program to find the square root of a number.
num = 49
sq_root = num**1
print(sq_root)

# 3.	Write a Python program to calculate the area of a circle.
r=2.5
area=3.14*r*r
print("Area of circle is: ",area)

# 4.	Write a Python program to convert kilometers to miles.
km=int(input("Enter the kilo meters: "))
miles=km*0.62
print(f"{km} kilo meter is = {miles} miles")
# 5.	Write a Python program to generate a random number between 1 and 10.
import random
x = random.randint(1,10)
y = random.random()
print(y)

# 6.	Create a variable called "name" and assign it your name.
name="Shaoib Ali Shahani"
print("Hello",name)

# 7.	Create a variable called "age" and assign it your age.
age=21
print("Shoaib Ali your age is: ",age)

# 8.	Create a variable called "pi" and assign it the value of pi (3.14159).
pi=3.14159
print("The value of pi = ",pi)

# 9.	Create two variables, "num1" and "num2," and assign them any two numbers. Print their sum.
a=1
b=4
sum=a+b
print(sum)

# 10.	Create a variable called "is_true" and assign it a boolean value of True.
is_true=True
print("I am married ",is_true)

# 11.	Create a variable called "message" and assign it a string of your choice.
message="Welcome to our first python program"
print(message)

# 12.	Print the length of the string stored in the variable "message."
print(len(message))

# 13.	Print the first character of the string stored in the variable "message."
print(message[0])

# 14.	Print the last character of the string stored in the variable "message."
print(message[-1])

# 15.	Print the string stored in the variable "message" in reverse.
print(message[-1::-1])

# 16.	Create a variable called "word" and assign it a string of your choice.
word=input("Enter your word: ")
print(word)

# 17.	Print the first three characters of the string stored in the variable "word."
print(word[0:3])

# 18.	Print the last three characters of the string stored in the variable "word."
print(word[-3:])

# 19.	Print every second character of the string stored in the variable "word."
print(word[1::2])

# 20.	Print the string stored in the variable "word" in reverse order.
print(word[-1::-1])

# 21.	Create a variable called "sentence" and assign it a sentence of your choice.
sentence="Welcome to our first program"
print(sentence)

# 22.	Print the sentence in all uppercase letters.
print(sentence.upper())

# 23.	Print the sentence in all lowercase letters.
print(sentence.lower())

# 24.	Print the number of occurrences of a specific word in the sentence.
lists=sentence.split()
length=len(lists)
print(f"The number of words in your senteces {length}")

# 25.	Replace a specific word in the sentence with another word and print the modified sentence
print(sentence.replace("first","second"))

# 26.	 Create three variables: "name," "age," and "city." Print a sentence using these variables to introduce yourself.
name="Shaoib"
age=21
city="Ghotki"
print(f"Hello! my name is {name} my age is {age} i am from {city}")

# 27.	Create a variable called "pi" and assign it the value of pi. Print the value of pi with two decimal places.
pi = 3.14159
pi_rounded = round(pi, 2)
print("The value of pi is:", pi_rounded)

# 28.	Create a variable called "num" and assign it any number. Print the number with leading zeros (e.g., 001, 002).
num = 7
formatted_num = "{:03}".format(num)
print(formatted_num)

# 29.	Create a variable called "price" and assign it a float value. Print the price in currency format (e.g., $10.99).
price = 10.99
formatted_price = "${:.2f}".format(price)
print(formatted_price)

# 30.	Create a variable called "percentage" and assign it a decimal value. Print the percentage with a percentage sign (e.g., 50%).
percentage = 0.5
formatted_percentage = "{:.0%}".format(percentage)
print(formatted_percentage)

# 31.	 Write a Python program to calculate the sum of the digits of a given number.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
sum=num1+num2
print("Sum of numbers: ",sum)

# 32.	Write a Python program to check if a number is prime or not.
prime=int(input("Enter the you want to check prime number or not: "))
is_prime=True
if prime<=1:
    is_prime=False
else:
    for i in range(2,prime):
        if prime%i==0:
            is_prime=False
            break
print(is_prime)

# 33.	Write a Python program to generate the Fibonacci sequence up to a specified number of terms.
no=int(input("Enter the number range: "))
a=0
b=1
c=0
i=0
while i<no:
    c=a+b
    a=b
    b=c
    i=i+1
    print(c)


# 34.	Write a Python program to find the factorial of a number.

num = int(input("Enter a number you want factorial: "))

factorial_result = 1
for i in range(1, num + 1):
    factorial_result *= i

print(f"The factorial of {num} is: {factorial_result}")

# 35.	Write a Python program to calculate the area of a triangle given its base and height.
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)

# 36.	Create a variable called "my_list" and assign it a list of integers.
my_list=[1,2,3,4,5,6,7,8]
print(my_list)

# 37.	Create a variable called "my_tuple" and assign it a tuple of strings.
my_tuple=("Welcome","to","My","tuple")
print(my_tuple)

# 38.	Create a variable called "my_set" and assign it a set of floating-point numbers.
my_set={12.3,34.2,23.5,12.3,53.3}
print(my_set)

# 39.	Create a variable called "my_dict" and assign it a dictionary with key-value pairs representing student names and their corresponding grades.
my_dict={
    "Sudhir" : "2nd Year",
    "Shaoib" : "1st Year",
    "Abid"   : "3rd Year"
}
print(my_dict)

# 40.	Create a variable called "my_bool" and assign it the result of a comparison between two numbers.
my_bool=True
a=1
b=2
if a==b:
    my_bool
print(my_bool)

# 41.	Create a variable called "text" and assign it a multiline string.
text="""
    Hello!
    This is Shaoib Ali Shahani
    Welcome to the my first program
    Bye
"""
print(text)
# 42.	Print each line of the multiline string stored in the variable "text" separately.
text1=text.split("\n")
print(text1)

# 43.	Count the number of occurrences of a specific character in the string stored in the variable "text."
chr="o"
count=text.count(chr)
print(f"The character '{chr}' appears {count} times in the text.")

# 44.	Check if a specific word is present in the string stored in the variable "text."
word="Ali"
word in text
print(word)
# 45.	Replace a specific substring in the string stored in the variable "text" with another substring.
text.replace("Ali","Ahmed")
print(text)
# 46.	Create a variable called "sentence" and assign it a sentence of your choice.
sentense=input("Enter your setence: ")
print(sentense)

# 47.	Print every alternate word in the sentence stored in the variable "sentence."
sent=sentense
sen=sent.split()
sent=sen[::2]
print(sent)

# 48.	Print the sentence stored in the variable "sentence" in reverse word order.
sent=sen[-1::-1]
print(sent)

# 49.	Extract the last four characters from the sentence stored in the variable "sentence."
index=sentense[-1:-5:-1]
print(index)

# 50.	Extract a substring from the sentence stored in the variable "sentence," starting from the third character and ending at the eighth character.
sentence = "This is an example sentence for the process."
substring = sentence[2:8]
print(substring)

# 51.	Print every alternate word in the sentence stored in the variable "sentence."
# 52.	Print the sentence stored in the variable "sentence" in reverse word order.
# 53.	Extract the last four characters from the sentence stored in the variable "sentence."
# 54.	Extract a substring from the sentence stored in the variable "sentence," starting from the third character and ending at the eighth character.
