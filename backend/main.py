from bs4 import BeautifulSoup
import requests
import re

MAX_CRAWL_PAGES = 2

def extract_words(content):
    # TODO
    # add stop words filter
    words = set()
    for word in content:
        if len(word) > 3 and len(word) < 15:
            words.add(word)
    return words

def extract_content(soup):
    text_elements = soup.find_all('p')
    content = ''
    for element in text_elements:
        content += f" {element.text}"

# add crawling logic

def extract_links(soup):
    internal_link_elements = soup.find_all('a', href=re.compile(r'^/news/articles/'))
    links = set()
    for link in internal_link_elements:
        set.add(link.get('href'))
    return links

def crawl_and_extract(start_url, output_file, max_pages=MAX_CRAWL_PAGES):
    html_content = requests.get(start_url).content
    soup = BeautifulSoup(html_content, 'html.parser')

    links = extract_links(soup)



if __name__ == "__main__":
    start_url = "https://www.bbc.com/news/articles/cn5yndv251qo"
    crawl_and_extract(start_url, 'swahili_corpus.txt')