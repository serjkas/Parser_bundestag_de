import requests
from bs4 import BeautifulSoup
import json

'''
persons_url_list = []
for i in range(0, 740, 20):
url = f'https://www.bundestag.de/ajax/filterlist/en/members/453158-453158?limit=20&noFilterSet=true&offset={i}'
#print(url)

q = requests.get(url)
result = q.content

soup = BeautifulSoup(result, 'lxml')
persons = soup.find_all(class_='bt-open-in-overlay')

for each in persons:
    person_page_url = each.get('href')
    persons_url_list.append(person_page_url)

with open('persons_url_list.text','a') as file:
for line in persons_url_list:
    file.write(f'{line}\n')
'''

with open('persons_url_list.text') as file:
    lines = [line.strip() for line in file.readlines()]

    data_list = []
    count = 0
    for line in lines:
        q = requests.get(line)
        # print(q)
        result = q.content
        # print(result)
        soup = BeautifulSoup(result, 'lxml')
        # print(soup)
        person = soup.find(class_='bt-biografie-name').find('h3').text
        peron_name_and_comany = person.strip().split(',')
        person_name = peron_name_and_comany[0]
        person_company = peron_name_and_comany[1].strip()

        social_links = soup.find_all(class_='bt-link-extern')

        social_links_list = []

        for item in social_links:
            social_links_list.append(item.get('href'))

        print(social_links_list)

        data = {
            'person_name': person_name,
            'person_company': person_company,
            'social_links': social_links_list

        }

        # print(data)
        count += 1
        print(f'{count}: {line} Выполнено!')

        data_list.append(data)

        with open('data.json', 'w') as json_file:
            json.dump(data_list, json_file, indent=4)
