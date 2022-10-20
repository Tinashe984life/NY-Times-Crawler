from bs4 import BeautifulSoup
import requests, webbrowser
from colorama import Fore

url = "https://www.nytimes.com/section/technology"

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')

links_list = []

stories_container = soup.find('div', class_='css-13mho3u')

stories = stories_container.find_all('li', class_='css-112uytv')

for story in stories:
    story_name = story.h2.text
    story_link = story.a.attrs['href']
    links_list.append(story_link)
    print(Fore.GREEN, story_name + ' -' + Fore.RED, story_link)

#def openLinks(link):
#    webbrowser.open(link)

