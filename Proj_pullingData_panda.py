from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')

table = soup.find_all('table')[1]

# world_titles = soup.find_all('th')
world_titles = table.find_all('th')

world_table_titles = [title.text.strip() for title in world_titles]

#print(world_table_titles)

df = pd.DataFrame(columns = world_table_titles)

#print(pf)

column_data = table.find_all('tr')

#for row in column_data:
    #row_data = row.find_all('td')
    #individual_row_data = [data.text.strip() for data in row_data]
    #print(individual_row_data)


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    #print(individual_row_data)
    length = len(df)
    df.loc[length] = individual_row_data

df.to_csv(r'E:\study\python\py_with_mysql\companies.csv', index= False)


table2 = soup.find_all('table', class_ = 'wikitable sortable')[2]


world_titles2 = table2.find_all('th')


world_table_titles2 = [titles.text.strip() for titles in world_titles2]

#print(world_table_titles2)

df2 = pd.DataFrame(columns = world_table_titles2)

column_data2 = table2.find_all('tr')

for each_row in column_data2[1:]:
    row_data2 = each_row.find_all('td')
    individual_row_data2 = [data2.text.strip() for data2 in row_data2]
    length2 = len(df2)
    df2.loc[length2] = individual_row_data2

df2.to_csv(r'E:\study\python\py_with_mysql\top10Companies.csv', index= False)