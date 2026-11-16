# Hardcoded values for the season and plant type
while True:
    try:
        season = input("Enter: 'summer' or 'winter'").lower()
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

# TODO: Replace with input() to allow user interaction.

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
