import datetime  # date library import to catch the current month no matter when you run the program


def main():

    # Current month object for this month
    current_month_fullname = get_current_month()

    # users input for name and BD month
    name = input('What is your name? ')
    birthday_month = input('What month is your birthday? ')

    # Input check - While there is no input for both either fields, present those prompts again until they write something. Maybe write a unit test or test case if the users writes another month name other than in the 12 months calender
    while not name or not birthday_month:
        print('Please enter both given fields to continue')
        name = input('What is your name? ')
        birthday_month = input('What month is your birthday? ')

    # 3 arguments this function takes in,users input of  name and birthday
    message_to_users(name, birthday_month, current_month_fullname)


# get month name whenever this program run now
# the now() is a method from datetime to get the time now, and 'strftime('%B')' will be able to grab the month's full name using the syntax, "%B" where "%b" gives abbreviated like Aug.
def get_current_month():
    # Return the current date time month when this program runs
    return datetime.datetime.now().strftime('%B')


# Function to call every time after users input to send them a message. This will show either a happy birthday message with their length of their names OR a simple greetings with their name length
def message_to_users(name, birthMonth, current_month_fullname):

    # Older version
    # To match with the current month format where the first letter of the month is capitalized
    # birthday_month.capitalize()
    # print(birthday_month.capitalize()) // Test print

    # Check if users birthday month is same as current month and case insensitive.
    # birthMonth == current_month_fullname
    if case_insensitive_comparison(birthMonth, current_month_fullname):
        print(f'Happy Birthday {name}! 🎉🎉🎉 Your name has {len(name)} letters!')
    else:
        print(f'Hello {name}! Your name has {len(name)}!')


# Case insensitive comparison function
def case_insensitive_comparison(birthMonth, current_month_fullname):
    return birthMonth.lower() == current_month_fullname.lower()


# Main function call
main()
