import os.path
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from shutil import *
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from datetime import datetime
import csv

# assign dates
todayDate = datetime.today().strftime('%d%m%Y_%H%M%S')
# backup flat file with date appended
bakFile = "listing_" + todayDate + ".csv"
# current flat file
my_file = "listing.csv"

# check if file exists, and backup the current file if found
if len(my_file) > 1:
    if os.path.exists(my_file):
        copyfile(my_file, bakFile)
        checkFile = open(my_file, "r+")
        checkFile.truncate()
        checkFile.close()

# extract the page content usign beautiful soup
def extract(page):
    # apply agent rotator (optional)
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    headers = {'User-Agent': user_agent_rotator.get_random_user_agent()}
    url =f'http:/www.xyz.com'
    r = requests.get(url,headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

# extract necessary data from the soup object and save into a flat file
def transform(soup):
    listing =[]
    # look for the tag with the class name
    container = soup.find_all('article', class_ ='listing--card')
    # loop through the container
    for item in container:
        # assign variable to the column
        col1 = item.get('data-listing-id')
        col2 = item.get('data-display-title')
        col3 = item.find('div', class_='listing__price').string
        # create a dictionary to hold the data
        list = {
                'col1' : col1,
                'col2' : col2,
                'col3' : col3,
        }
        # append the dictionary line by line
        listing.append(list)
        # write into flat ile
        with open(my_file,'a') as csv_file:
            writer = csv.writer(csv_file)
            for list in listing:
                writer.writerow(list)
    return

# loop through the pages using the function defined above
for i in range (start, end,-1):
    print(f'Getting page, {i}')
    c = extract(i)
    transform(c)
    sleep(randint(7,10))

print('Completed!')
