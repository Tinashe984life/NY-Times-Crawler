from bs4 import BeautifulSoup
import requests
from colorama import Fore

url = "https://www.nytimes.com/section/technology"

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')

links_list = []

stories_container = soup.find('div', class_='css-13mho3u')

stories = stories_container.find_all('li', class_='css-112uytv')

for story in stories:
    story_name = story.h2.text
    print(Fore.GREEN, story_name)

#print(Fore.RED, story)

