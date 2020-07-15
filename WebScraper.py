from bs4 import BeautifulSoup
import requests

all_courses = {}


URL = 'https://www.uvu.edu/catalog/current/courses/biology/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='courses-container')

courses = results.find_all('div', class_='course')

for course in courses:

    all_courses[course.find('div', class_='class_title').text] = course.find('div', class_='section_number').text.strip()


print(all_courses)


