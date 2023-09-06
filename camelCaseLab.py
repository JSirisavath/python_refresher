import re  # regex import library


# Test cases
text = "HELLO World"

text2 = "Beautiful mistakes"

text3 = "Beauty-Behind-Madness"

text4 = "my dear    -melancholy"

text5 = "La SANta"

text6 = "#232 apartment "


# Convert Strings to camel case
def convert_strings_to_camel_case(text):
    # Using regex, find all upper case letters first with lower case letters
    words = re.findall(r"[A-Z][a-z]*|[A-Z]+|[a-z]+", text.lower())

    # Convert the first word of the list made to lower case, where that word is contain in its own list element so e.g. ['hello']
    # Join with another list element, this is a list comprehension, another way to create a list
    # Use for loop starting at the second word. Slice start at 1 and : is however many words there are to the end and capitalize the first letter
    # Join their respective separate array together e.g ['hello']+['World'] = ['hello','World']
    # Second word and onward inside list is capitalized
    camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]

    return "".join(camel_case_words)  # 'hello'+ World = helloWorld


# Banner function
def banner():
    """Display program name"""
    message = "Awesome camel case program!"

    stars = "*" * len(message)

    print(f"\n{stars}\n{message}\n{stars}\n")


# Instructions function
def instructions():
    """Print instructions"""
    print("Enter a sentence and this program will convert it to camel case.")


# Main function
def main():
    # banner display at first
    banner()

    # Instructions to users
    instructions()

    # Users input text
    text = input("Enter your text here: ")

    # Output text
    output = convert_strings_to_camel_case(text)

    # Print output text here to terminal
    print(output)

    # Note, the function will not work for ambiguous words formatted like "mydearmelancholy" - This might be a specific case handler


# Calling main
if __name__ == "__main__":
    main()
