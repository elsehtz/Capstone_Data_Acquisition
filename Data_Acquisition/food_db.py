import requests
import os.path

# Input  c
parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
path = parent_path + "/Data/input.txt"
file = open(path, "r")
text = file.read()

# Model

    # What do you want the model to do?
    #   I want it to take in a list of foods and generalize it
    #   hard coding a bank of foods primary food types
# +++PLAN+++
    # Get a corpus of brand and foods from FDA food db
    # Train model to remove brands based on common words from FDA
    # (A kind of rare word removal)

# Web scrape for each expiraion date & append

# We will need a local db for generalized food

# Send out
# [
#     {
#         "Food": "chicken",
#         "Calories":"/g",
#         "Protein":"/g",
#         "Fat":"/g",
#         "Carbs":"/g",
#         "Expiration days":"days",
#     },
# ]

#===================================================================================
#===================================================================================

# Receive data through API
response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)

# Send data through API
with open('report.xls', 'rb') as f:
    r = requests.post('http://httpbin.org/post', files={'report.xls': f})

#===================================================================================
#===================================================================================

# STEPS:
# Get food list
# Put into model
# Food generalized into df
# get expiration dates for each row
# out to db (as json?)