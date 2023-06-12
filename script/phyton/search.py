import requests
from bs4 import BeautifulSoup

def search(query):
    url = 'https://www.google.com/search?q=' + query
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                'title': title,
                'link': link
            }
            results.append(item)
    return results