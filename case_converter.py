def main():
    """
    Python script to get a sentence from a user and converts the
    user input into the appropriate sentence case
    """
    # Get the sentence from the user
    sentence = input("Please enter your sentence to convert and press enter when done: ")
    print("")
    # Print the available options for conversion
    print(""" 
    1. Uppercase (THIS SENTENCE IS IN UPPERCASE)
    2. Lowercase (this sentence is in lowercase)
    3. Titlecase (This Sentence Is In Titlecase)
    4. Camelcase (ThisSentenceIsInCamelcase)
    5. Snakecase (this_sentence_is_in_snakecase)
    6. Capitalize (This sentence is in capitalize)
    """)
    # create dictionary of available options
    choice_dict = {
        "1": "uppercase",
        "2": "lowercase",
        "3": "titlecase",
        "4": "camelcase",
        "5": "snakecase",
        "6": "capitalize"
    }
    # convert distionary keys to a list for use in logic to validate user conversion choice is correct
    keys = list(choice_dict.keys())
    # Get conversion choice from user
    choice = input("Select the type to convert to (type equivalent number and press enter): ")
    # Logic to verify conversion choice is correct
    while choice not in keys:
        choice = input("Please type in one number representing your choice from the list above: ")
    choicetaken = choice_dict[choice]
    # clear the screen
    print("\n" * 15)
    converted_sentence = convertcase(choicetaken, sentence)
    print("The sentence you want converted to " + choicetaken + " is " + '"' + sentence + '"')
    print("")
    print("Here is your converted sentence - " + '"' + converted_sentence + '"')
    print("")
    print("")


# function to make the sentence conversion
def convertcase(choicetaken, sentence):
    # conver to uppercase
    if choicetaken == "uppercase":
        sentence = sentence.upper()
    # conver to lowercase
    if choicetaken == "lowercase":
        sentence = sentence.lower()
    # convert to titlecase
    if choicetaken == "titlecase":
        sentence = sentence.title()
    # convert to capitalize
    if choicetaken == "capitalize":
        sentence = sentence.capitalize()
    # convert to camelcase
    if choicetaken == "camelcase":
        temp = sentence.title()
        temp_list = temp.split()
        sentence = ""
        for i in range(len(temp_list)):
            sentence += temp_list[i]
    # convert to snakecase
    if choicetaken == "snakecase":
        temp = sentence.lower()
        temp_list = temp.split()
        sentence = ""
        for i in range(len(temp_list) - 1):
            sentence += temp_list[i] + "_"
        sentence = sentence + temp_list[-1]
    return sentence


if __name__ == "__main__":
    main()