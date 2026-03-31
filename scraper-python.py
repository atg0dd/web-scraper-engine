import requests
from bs4 import BeautifulSoup

def scrape():
    url = 'https://global.hanyang.ac.kr/s3/s3_4.php'
    
    # sends an HTTP GET request to the url
    response = requests.get(url)

    '''
        response.text - the raw HTML content of the page as a string
        BeautifulSoup(..., 'html.parser') -- parses the HTML into a navigable tree structure
        now soup lets me search/extract element like soup.find('div'), soup.find_all('a') etc
    '''
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)

if __name__ == '__main__':
    scrape()
