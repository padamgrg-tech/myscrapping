import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://realpython.github.io/fake-jobs/')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

job_position = []
comapny_name = []
job_location = []

for item in soup.find_all('h2', attrs={'class':'title is-5'}):
    # print(item.text)
    job_position.append(item.text)
# print(job_position)

for item in soup.find_all('h3', attrs={'class':'subtitle is-6 company'}):
    comapny_name.append(item.text)
# print(comapny_name)

for item in soup.find_all('p', attrs={'class':'location'}):
    job_location.append(item.text)
# print(job_location)

data = {"Job Position":job_position,
        "Company Name":comapny_name,
        "Job Location":job_location
        }
# print(data)
    
data_table = pd.DataFrame(data) # to change data into table
# print(data_table)

data_table.to_excel("jobdata.xlsx")