import requests, bs4
import re
import json
from bs4 import BeautifulSoup

URL = 'https://www.ssa.gov/oact/babynames/top5names.html'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 
request = requests.get(URL, headers=headers)
soup = BeautifulSoup(request.content, 'html5lib')
table_rows = soup.findAll('tr')
rows = []
for row in table_rows:

    rows.append(row)

names = {}
del rows[1]
del rows[0]
for row_item in rows:

    
    try:
        delimiters = '<td>', '</td>', '<tr>', '</tr>', '<td align="center">', '\n'
        regex_pattern = '|'.join(map(re.escape, delimiters))
        list_item = re.split(regex_pattern, str(row_item))
        delete = [0, 0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]
        for i in delete:
            del list_item[i]

        female_indexes = [1, 2, 3, 4, 5]
        male_indexes = [6, 7, 8, 9, 10]

        females = []
        males = []
        for i in female_indexes:
            females.append(list_item[i])
        for i in male_indexes:
            males.append(list_item[i])

        names[list_item[0]] = ([females])
        names[list_item[0]] += ([males])
    

        
    except Exception as e:
        print(e)

print()
print()
print(names)
print(names['1928'][0])

with open("names.json", "a") as file:
    json.dump(names, file)