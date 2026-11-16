# Garden advice application
'''
This application provides gardening advice for the users requirements.
The program accepts user input and returns statements printed to the console
'''


# Accept user input for season with try-except
def get_season():
    '''
    Value error is returned if non-string input is entered.
    User input is validated against a list of values
    '''
    while True:
        try:
            season = input("Enter: 'summer' or 'winter': ").lower()
            # TODO: Replace with input() to allow user interaction.
        except ValueError as error:
            print("Input invalid")
            print(error)
        valid_inputs = ['summer', 'winter']
        if season not in valid_inputs:
            print("Please enter a valid season")
            continue
        else:
            break
    return season


# Accept user input for plant type with try-except
def get_plant_type():
    '''
    Value error is returned if non-string input is entered.
    User input is validated against a list of values
    '''
    while True:
        try:
            plant_type = input("Enter 'flower' or 'vegetable': ").lower()
        except ValueError as error:
            print("Invalid input")
            print(error)
        valid_inputs = ['flower', 'vegetable']
        if plant_type not in valid_inputs:
            print("Please enter a valid plant type")
            continue
        else:
            break
    return plant_type


def get_advice(season, plant_type):
    # Variable to hold gardening advice
    advice = ""

    # Determine advice based on the season
    '''
    Acceptable seasons are "summer" or "winter".
    Advice is returned accordingly
    '''
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"

    # Determine advice based on the plant type
    '''
    Acceptable seasons are "flower" or "vegetable".
    Advice is returned accordingly.
    '''
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."

    # Print the generated advice
    print(advice)


while True:
    choice = int(input("Enter '1' to proceed or '0' to exit: "))
    if choice == 1:
        season = get_season()
        plant_type = get_plant_type()
        get_advice(season, plant_type)
        continue
    elif choice == 0:
        print("See you later")
        break
    else:
        print("Select a valid choice")
        continue


# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
