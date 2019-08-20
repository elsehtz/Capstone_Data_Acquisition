# Zakary ElSeht
# 8/12/2019
#
#

#===========================================================
# IMPORTS
#===========================================================
import re
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#===========================================================
def main():
    # Get the html from the site using beautiful soup
    url = 'http://<website>.<info>/<request>.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Do Stuff
    # ex: regex here 
    # Open a webpage
    response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
    html = response.read()

    # Extrct only the text from the site
    soup = BeautifulSoup(html,'html.parser')
    text = soup.get_text(strip = True)

    # Save raw text to a file

    # Add a pause to not spam the website with requests
    time.sleep(1)

if __name__ == "__main__":
    main()
