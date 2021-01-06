import requests
import re
import nltk
nltk.download('stopwords')
from bs4 import BeautifulSoup as soup

class NewsParser:

    def __init__(self, url):
        self.url = url

    def get_news(self):
        uClient = requests.get(self.url)
        page_html = uClient.content
        uClient.close()
        page_soup = soup(page_html, 'html.parser')
        content_raw = page_soup.findAll('p', {'class': 'content-text__container'})
        return content_raw

    def content_raw_to_phrases(self):
        """
        função que separa o texto em um array de frases
        """
        phrases_array = []
        for paragraph  in self.get_news():
            for prhase in re.sub(r"[()\"/;:<>{}+=~|!?]", '', paragraph.text.lower().replace('. ', '.').replace(', ', ' ')).split('.'):
                if prhase:
                    phrases_array.append(prhase)
        return phrases_array

    @staticmethod
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

    def generate_phrases_array(self):
        """
        função que unifica o array de palavras de cada frase, retornando uma matriz de palavras.
        """
        phrases_array = []
        for phrase in self.content_raw_to_phrases():
            phrases_array.append(self.phrase_to_words(phrase))
        return phrases_array
        
    def count_words(self):
        """
        função que retorna a frequência em forma de dicionário de cada palavra existente no texto.
        """
        dictionary = {}
        for n in self.generate_phrases_array():
            for i in n:
                try:
                    dictionary[i] += 1
                except Exception as e:
                    dictionary[i] = 1
        return dictionary

    def rank_words(self):
        """
        função que retorna um array de tuplas, na ordem crescente, a frequência de palavras no texto.
        """
        sort_value = {}
        sort_value = sorted(self.count_words().items(), key=lambda x: x[1], reverse=True)
        return sort_value

    def __repr__(self):
        return f'<NewsParser of: {self.url}>'

#link da notícia usada no programa:
#'https://g1.globo.com/economia/noticia/2020/07/27/dolar.ghtml'