# simple variables, numbs, booleans, and strings practice

print('Hello World!')

hello = 'hello'

letterH = hello.startswith('h')

print(letterH) # True 

name = "Jay Sirisavath"

age = 22

student = True

print(name, "Age:", age,  "Are you a student?", student) 

# New line format method version
print("Name: {}, Age: {}, New Patient? {}".format(name, age, student))


# Input 
# Input your name
users_name = input("What is your name? ")

print("Hello, {}!".format(users_name))