from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://trojanconstruction.group/en/projects/COMPLETED').text
soup = BeautifulSoup(source,'html.parser')

# print(soup.prettify())
file = 'projects_data.csv'
csv_file = open(file, 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['projects name', 'project img'])

for item in soup.find_all('div', class_='projects_img'):
    project_img = item.find('img')['src'].strip()
    project_name = item.find('h2').text

    csv_writer.writerow([project_name, project_img])

    # print(project_name, '|' ,project_img_src)
    # print('-----------------------------------------------')
csv_file.close()

