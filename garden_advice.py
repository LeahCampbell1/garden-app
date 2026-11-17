# Garden advice application
'''
This application provides gardening advice for the users requirements.
The program accepts user input and returns statements printed to the console
'''


# Accept user input for season with try-except
def get_season():
    '''
    Value error is returned if input or format is invalid.
    User input is validated against a list of values
    '''
    while True:
        try:
            season = input("Enter: 'summer' or 'winter': ").lower()
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
    Value error is returned if input or format is invalid.
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


# Define function to output planting advice to user
def get_advice(season, plant_type):
    '''
    Advice for user input is generated in this function.
    Inputs from get_season() and get_plant_type() are passed as variables.
    '''
    # Variable to hold gardening advice
    advice = ""
    advice_statement = [
        'Water your plants regularly and provide some shade.\n',
        'Protect your plants from frost with covers.\n',
        'No advice for this season.\n',
        'Use fertiliser to encourage blooms.\n',
        'Keep an eye out for pests!\n',
        'No advice for this type of plant.\n']

    # Determine advice based on the season
    # Acceptable seasons are "summer" or "winter".
    # Advice is returned accordingly

    if season == "summer":
        advice += advice_statement[0]
    elif season == "winter":
        advice += advice_statement[1]
    else:
        advice += advice_statement[2]

    # Determine advice based on the plant type
    # Acceptable plat types are "flower" or "vegetable".
    # Advice is returned accordingly.

    if plant_type == "flower":
        advice += advice_statement[3]
    elif plant_type == "vegetable":
        advice += advice_statement[4]
    else:
        advice += advice_statement[5]

    # Print the generated advice
    print(advice)


# Define function to recommend planting option to user
def get_recommendation(season, plant_type):
    '''
    Prints recommendation to reader on what to plant based on original input
    Recommendations from:
    https://www.gardenersworld.com/how-to/grow-plants/eight-plants-that-flower-all-summer/
    '''
    plant = [
        "Geranium ‘Rozanne’ or Agapanthus (African Lily)",
        "Lettuce or Carrots",
        "Snowdrops or Pansies",
        "Parsnips or Kale"
    ]
    if season == "summer" and plant_type == "flower":
        print(plant[0])
    elif season == "summer" and plant_type == "vegetable":
        print(plant[1])
    elif season == "winter" and plant_type == "flower":
        print(plant[2])
    elif season == "winter" and plant_type == "vegetable":
        print(plant[3])


# Welcome message for application
welcome_message = '''
    Welcome to the gardening app. If you enter the details for the season
    and plant type you require, advice will be generated for you.
    '''

# Prints welcome message to user
print(welcome_message)

# While loop delivers program choices for user interaction
while True:
    choice = int(input("Enter '1' to proceed or '0' to exit: "))
    if choice == 1:
        season = get_season()
        plant_type = get_plant_type()
        get_advice(season, plant_type)
        print("Advice on what to plant:\n")
        get_recommendation(season, plant_type)
        continue
    elif choice == 0:
        print("See you later")
        break
    else:
        print("Select a valid choice")
        continue
