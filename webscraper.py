import requests
import pandas as pd
from bs4 import BeautifulSoup

web_url = 'https://www.zyxware.com/articles/5914/list-of-fortune-500-companies-and-their-websites-2018'
response = requests.get(web_url)

#print('Status code\n', response.status_code)
#print('\n--\n')
#print('Content of the website\n', response.content[:2000])

soup_object = BeautifulSoup(response.content, 'html.parser')

# Uncomment the below line and look into the contents of soup_object
#soup_object

data_table = soup_object.find_all('table', 'data-table')[0]

all_values = data_table.find_all('tr')
all_values[:10] # Prints the first 10 captured tag elements

print(all_values[0])
print('--')
print(all_values[1])
print('--')
print(all_values[2])

##

fortune_500_df = pd.DataFrame(columns = ['rank', 'company_name', 'company_website']) # Create an empty dataframe
ix = 0 # Initialise index to zero

for row in all_values[1:]:
    values = row.find_all('td') # Extract all elements with tag <td>
    # Pick only the text part from the <td> tag
    rank = values[0].text
    company = values[1].text
    website = values[2].text

    fortune_500_df.loc[ix] = [rank, company, website] # Store it in the dataframe as a row
    ix += 1

# Print the first 5 rows of the dataframe
x = fortune_500_df.head()
print(x)

fortune_500_df.to_csv('fortune_500_companies.csv', index=False)

