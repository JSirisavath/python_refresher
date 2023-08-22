# Python basics and refreshers

# Variables
school = 'MCTC'
gpa = 3.8
students_in_class = 22


# if statements
# use ':' after the condition
# Make sure to indent after the condition
if gpa == 4:
    print('WOW!')

elif gpa > 3:
    print('Awesome!')

else:
    print('Cool!')


# Data structures - In python, they are called  sequences, in other words iterables I think, at least in JavaScript
# Lists
schools = ['MCTC', 'Dakota CTC', 'North Hennepin Tech College']

# If referencing the schools with a specific variable
if 'MCTC' in schools:
    print('This is our school in the list!')

# Sorting inside this school lists
schools.sort()
print(schools)

# Add to lists

# Will add to the end of the list
schools.append('Century College')

print(schools)

# Reverse lists

schools.reverse()  # will return value of non or null if you put print() outside while schools.sort() is firing off

print(schools)


# Strings
class_name = 'software Development Capstone'

# Strings methods
# This will make the first character of the first letter inside a string be capitalized, in this case, "Software"
print(class_name.capitalize())

# Keep in mind, when using methods such as this, some require to type in the argument into the method instead of `variable name`.length()

print(len(class_name))  # length of letters inside a string

# It seems like split method doesn't mutate the original copy
# Will create an array - break up letters or words by starting with this argument, 'a'
print(class_name.split('a'))


if 'Capstone' in class_name:
    print('This must be the capstone')

# Loops - Since strings are sequences as well, we can loop through each character too
for word in class_name:
    print(word.upper())

# Printing words from strings and multiplying with their strings
for letter in school:
    print(letter*10)

# ranges in loops
for x in range(10):
    print(x+1)

# Fill in's with 0 inside 10 x's [0,0,0,0,0,0,etc]
data = [0] * 10

print(data)

more_data = ['None']*10

print(more_data)

value_to_replace = 'None'
new_value = 'Fill'

for index in range(len(more_data)):
    # print(more_data[index])
    if more_data[index] == value_to_replace:
        # print('This is working')
        more_data[index] = new_value

print(more_data)


# While loops - Do something while there is still data to process
name = input('Enter your name: ')

# First version of the while loop
# while len(name) == 0:
# print('Please enter at least 1 character')
# name = input('Enter your name: ')

# Another way to write while loop condition
# The not reference is same thing as "!name" in other languages
while not name:
    print('Please enter at least 1 character')
    name = input('Enter your name: ')

if name:
    print("Hello, {}!".format(name))

# Booleans
start_of_semester = True
winter = False

if winter:
    print('brrr!')
else:
    print('It is not winter')


# Dictionaries - Basically objects

class_codes = {2905: 'Capstone', 2560: 'Web Client and Servers', 2545: 'Java'}

# What is a specific class based on the code inside an object?
print('This class is {}'.format(class_codes[2560]))

for code in class_codes:
    # Class codes or just the keys
    print("class code: {}".format(code))

    # class names or the values
    print(class_codes[code])


# Keys and values together
# Kind of like destructuring inside the for loops
# str to convert numbers to strings
for code, class_name in class_codes.items():
    # print('This class code is {} and the class name is {}'.format(str(code), class_name))

    # Can also use f in the beginning to format
    print(f'This class code is {code} and the name is {class_name}')


# Slicing strings inside an array
schools = ['MCTC', 'Dakota CTC', 'North Hennepin Tech College']

# Slicing to get the first 2 schools
first_two_schools = schools[0:2]  # start at first end for the 2nd element
# Another shortcut is this [:2], the ':' will assume you want to start at the beginning and referencing exclusive for the end

print(first_two_schools)

print(schools)

# Keep in mind, it does not mutate the original
school_name = 'Minneapolis Community and Technical College'

city = school_name[:11]  # Will slice and give Minneapolis for city

# Getting last element
# For backwards, the start or inclusive is the negative number of each letters
type_of_school = school_name[-7:]

# print(city)
print(type_of_school)
# print(school_name)


# File IO
with open('data.txt') as f:
    print(f.read())

# Write to file
with open('schools.txt', 'w') as f:
    for school in schools:
        f.write(school+'\n')


# Functions
def get_users_name():
    print('Hello, please enter your name!')
    users_name = input('Name: ')

    return users_name


# Calling
print(f'Hi, {get_users_name()}')
