from bs4 import BeautifulSoup

def parse_results(html, keyword):
    soup = BeautifulSoup(html, 'html.parser')
 
    found_results = ''
    rank = 1
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:
 
        link = result.find('a', href=True)
        title = result.find('h3', attrs={'class': 'r'})
        description = result.find('span', attrs={'class': 'st'})
        if link and title:
            link = link['href']
            title = title.get_text()
            if description:
                description = description.get_text()
            if link != '#':
                found_results = found_results+str(description)
    return found_results
