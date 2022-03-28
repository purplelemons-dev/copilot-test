#usr/bin/env python3
# Path: test6.py
# Purplelemons-dev
# This program will search google for a given search term and print the results

import requests
from bs4 import BeautifulSoup


def get_google_results(search_term)->list[dict[str,str]]:
    url = 'https://www.google.com/search?q=' + search_term
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Split into seperate result sections
    parsed=soup.find_all('div', attrs={'class': 'ZINbbc luh4tb xpd O9g5cc uUPGi'})
    results = []
    for result in parsed:
        link = result.find('div', attrs={'class': 'egMi0 kCrYT'}).a
        title = result.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'})
        description = result.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
        results.append({
            'link': link,
            'title': title,
            'description': description
        })
    return results


# Format the results
def format_result(link, title, description):
    print('Link: https://www.google.com' + link.get('href'))
    print('Title: ' + title.text)
    print('Description: ' + description.text)
    print()

# Save a google search result to a file
def save_result(search,filename='result.html'):
    url="https://www.google.com/search?q="+search
    response = requests.get(url)
    with open(filename, 'w') as f:
        f.write(response.text)


if __name__ == '__main__':
    #print(get_google_results('python'))
    #save_result('python')
    for result in get_google_results('python'):
        format_result(**result)
