import requests
from bs4 import BeautifulSoup

# Pages to scrape — add more Hanyang URLs here
URLS = [
    'https://global.hanyang.ac.kr/s1/s1_1.php',  # 국제처 소개
]

def fetch(url) -> BeautifulSoup | None:
    """Fetch an html from input url and return BeautifulSoup object"""
    try: 
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'lxml')

    except requests.RequestException as exc:
        print(f"Failed to fetch {url}: {exc}")
        return None

def extract_text(soup: BeautifulSoup) -> str:
    for tag in soup.select('nav, header, footer, script, style'):
        tag.decompose()

    content = soup.select_one('.content, main, #content')

    target = content if content else soup.body

    return target.get_text(separator='\n', strip=True)

def scrape_all(urls):
    result = []

    for url in urls:
        soup = fetch(url)
        text = extract_text(soup)
        result.append({
            'url': url,
            'title': soup.title.get_text(strip=True) if soup.title else 'No Title',
            'text': text
        })
    
    return result 


def main():
    print("Starting to Scrape Web")

    pages = scrape_all(URLS)

    for page in pages:
        print(f"\n-- {page['title']} ---")
        print(page['text'][:500])

    print("Task Completed")

if __name__ == '__main__':
    main()
