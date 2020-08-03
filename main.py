import requests
import re
import nltk
nltk.download('stopwords')
from bs4 import BeautifulSoup as soup

def get_news(url):
    uClient = requests.get(url)
    page_html = uClient.content
    uClient.close()
    page_soup = soup(page_html, 'html.parser')
    content_raw = page_soup.findAll('p', {'class': 'content-text__container'})
    return content_raw

def content_raw_to_phrases(content_raw):
    """
    função que separa o texto em um array de frases
    """
    phrases_array = []
    for paragraph  in content_raw:
        for prhase in re.sub(r"[()\"/;:<>{}+=~|!?]", '', paragraph.text.lower().replace('. ', '.').replace(', ', ' ')).split('.'):
            if prhase:
                phrases_array.append(prhase)
    return phrases_array

def phrase_to_words(phrase):
    """
    função que separa uma frase em um array de palavras
    """
    stop_words = nltk.corpus.stopwords.words('portuguese')
    word_array = []
    for word in phrase.split(' '):
        if word and not word in stop_words:
            word_array.append(word)
    return word_array

def generate_phrases_array(phrases):
    """
    função que separa um
    """
    phrases_array = []
    for phrase in phrases:
        phrases_array.append(phrase_to_words(phrase))
    return phrases_array
    
def count_words(phrases_array):
    dictionary = {}
    for n in phrases_array:
        for i in n:
            try:
                dictionary[i] += 1
            except Exception as e:
                dictionary[i] = 1
    return dictionary

def rank_words(dictionary):
    sort_value = {}
    sort_value = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sort_value

def main():
    content_news = get_news("https://g1.globo.com/economia/noticia/2020/07/27/dolar.ghtml") 
    array_of_phrases = content_raw_to_phrases(content_news)
    matrix_of_words = generate_phrases_array(array_of_phrases)
    count_of_words = count_words(matrix_of_words)
    ranked_words = rank_words(count_of_words)

    print(content_news)
    print(array_of_phrases)
    print(matrix_of_words)
    print(count_of_words)
    print(ranked_words)

if __name__ == "__main__":
    main()


#'https://g1.globo.com/economia/noticia/2020/07/27/dolar.ghtml'