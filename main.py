import requests
import re
from bs4 import BeautifulSoup as soup

def get_news(url):
    uClient = requests.get(url)
    page_html = uClient.content
    uClient.close()
    page_soup = soup(page_html, 'html.parser')
    content_raw = page_soup.findAll('p', {'class': 'content-text__container'})
    return content_raw

def content_raw_to_array(content_raw):
    text_array = []
    for content in content_raw:
        for word in re.sub(r"[()\"/;:<>{}+=~|!?]", '',
                    content.text.lower().replace('. ', ' ').replace(', ', ' ') ).split(' '):
            text_array.append(word)
    return text_array

def count_words(text_array):
    dictionary = {}
    for key in text_array:
        try:
            dictionary[key] += 1
        except Exception as e:
            dictionary[key] = 1
    return dictionary

def rank_words(dictionary):
    sort_value = {}
    sort_value = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sort_value

def main():
    content_news = get_news("https://g1.globo.com/economia/noticia/2020/07/27/dolar.ghtml") 
    array_of_words = content_raw_to_array(content_news)
    count_of_words = count_words(array_of_words)
    ranked_words = rank_words(count_of_words)

    print(ranked_words)

if __name__ == "__main__":
    main()


#'https://g1.globo.com/economia/noticia/2020/07/27/dolar.ghtml'