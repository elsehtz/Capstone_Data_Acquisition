# Zakary ElSeht
# 8/12/2019
#
#

#===========================================================
# IMPORTS
#===========================================================
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import os.path
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
#===========================================================


# Use on first time run
#nltk.download()

# count_vect = CountVectorizer()


#===========================================================
# Utilizes variable name 'text' and parses that data
#===========================================================
# get text source:
parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
path = parent_path + "/Data/data.txt"
file = open(path, "r")
text = file.read()

# Tokenize text
tokens = [t for t in text.split()]
# Get count (countVecotirzation?)

# Get list of english stopwards 
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        # if token matches any english stopwards (a, it, etc.), remove it
        clean_tokens.remove(token)
 
freq = nltk.FreqDist(clean_tokens)
# for key,val in freq.items():
    # print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)
# X_train_counts = count_vect.fit_transform(twenty_train.data)
# X_train_counts.shape

# MySQL
# Endpoint: database-1.cmnixox8v3fi.us-east-1.rds.amazonaws.com
# Port: 3306
# Username: teamw4
# Password: wordPass123!

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   passwd="yourpassword",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [("John", "Highway 21"), ("Sal", "Warren 11")]
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")