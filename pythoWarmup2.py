
# Main method
def main():
    # Setting up the array to put users class in
    classes_you_are_taking = []

# Input for users to type in their classes
    users_class_inputs = input(
        'Type in a class you are taking this semester.\n When you are done typing in your classes, press enter: ')

# While data is still processing, add the class inside the list and then keep asking
    while users_class_inputs != '':
        classes_you_are_taking.append(users_class_inputs)
        users_class_inputs = input(
            'Type in a class you are taking this semester: ')

     # If the input is empty, then print those classes on each line
    print('The classes you are taking are:')
    # for user_class in classes_you_are_taking:
#     print(user_class)

    # Can also have the index of each variable
    # enumerate is to allow the compiler to unpack values. If I just put index +1, it will error
    for index, user_class in enumerate(classes_you_are_taking):
        print(f'{index+1} : {user_class}')


main()
