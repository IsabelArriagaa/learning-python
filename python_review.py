# Name: Isabel Arriaga Ayala 
print ("It worked!")

# x = none --> to create abyss 
x = 3
# The variable called [insert variable name here] is now holding the [data type] value [value].
example = "I'm a string" # The variabel called example is now holding the string value "I´m a string!"
a = 3 # The variable called a is now holding the integer value 3
b = 4.0 # The variable called b is now holding the flaot value 4.0
c = True # The variable called c is now holding the boolean value True
d = False # The variable called d is now holding the boolean value False
e = "Hey!" # The variable called e is now holding the string value "Hey!"
f = None # The variable called f is now holding the abyss (absence of a) value None
age = 32 # The variable called age is now holding the integer value 32
name = "Insert your name here" # The variable called name is now holding the string value "Insert your name here"
instrument = "Insert your instrument here" # The variable called instrument is now holding the string value "Insert your instrument here" (both of these could be great for an input value! aha !)

# The input from the user is valuable so you wanna have user put it in only once 

# prompt = "Enter your name"
# response = input(prompt)
# print("Hello,", response)
# print(response, "here is your agenda for the day...")

# userName = "Enter your name "
# nameResponse = input(userName)
# userAge = "Enter your age "
# ageResponse = input(userAge)
# print("Hello, ", nameResponse, "aged", ageResponse, "whose datatypes are", type(nameResponse), "and ", type(ageResponse))

# #Ask user for two numbers
# first_number = input("What's the first number?")
# second_number = input("What's the second number?")

# #Convert numbers to integer versions of themselves
# first_number = int(first_number)
# second_number = int(second_number)

# #Compare the two numbers
# if first_number > second_number:
#     print(first_number, "is bigger")
# elif first_number == second_number:
#     print("the numbers are equal!!!")
# else:
#     print(second_number, "is bigger")

name = input("What's your full name?")
length_of_name = len(name)
print(length_of_name)

while " " in name:
    name = name.replace(" ", "")

length_of_name = len(name)
print(length_of_name)