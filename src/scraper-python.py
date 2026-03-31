import requests
from bs4 import BeautifulSoup

def scrape():
    url = 'https://global.hanyang.ac.kr/s3/s3_4.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 1 — remove all noise first
    for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
        tag.decompose()

    # Step 2 — find the main content section
    # from the HTML we can see the content is inside <section class="s34">
    main = soup.find('section', class_='s34')

    # Step 3 — extract the page title
    title = soup.find('h3', class_='sub-tit-h3')
    print("=== PAGE TITLE ===")
    print(title.text.strip())

    # Step 4 — extract all section headings
    print("\n=== HEADINGS ===")
    for heading in main.find_all(['h3', 'h4', 'h5']):
        text = heading.text.strip()
        if text:
            print(f"{heading.name}: {text}")

    # Step 5 — extract all tables
    print("\n=== TABLES ===")
    for table in main.find_all('table'):
        for row in table.find_all('tr'):
            cells = row.find_all(['th', 'td'])
            row_data = [cell.text.strip() for cell in cells]
            if any(row_data):  # skip empty rows
                print(' | '.join(row_data))
        print("---")

    # Step 6 — extract all paragraph text
    print("\n=== CONTENT ===")
    for p in main.find_all('p'):
        text = p.text.strip()
        if text:
            print(text)

    # Step 7 — extract all links
    print("\n=== LINKS ===")
    for a in main.find_all('a', href=True):
        text = a.text.strip()
        href = a['href']
        if text:
            print(f"{text} → {href}")

if __name__ == '__main__':
    scrape()