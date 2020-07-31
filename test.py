import unittest
from bs4 import BeautifulSoup as soup
from main import get_news, content_raw_to_array, count_words, rank_words

class TestScrapping(unittest.TestCase):

    def test_get_news(self):
        url = 'https://g1.globo.com/economia/noticia/2020/07/27/dolar.ghtml'
        response = get_news(url)
        self.assertIsInstance(response, list)

    def test_content_raw_to_array(self):
        data = open('html_test.html', 'r')
        content_raw = soup(data, 'html.parser').findAll('p', {'class': 'content-text__container'})
        response_test = ['dólar', 'fechou', 'forte', 'queda', 'nesta', 'segunda-feira',
                        '27', 'dia', 'fraqueza', 'moeda', 'norte-americana', 'exterior',
                        'meio', 'tensões', 'diplomáticas', 'estados', 'unidos', 'china',
                        'investidores', 'modo', 'espera', 'antes', 'reunião', 'política',
                        'monetária', 'federal', 'reserve', 'bc', 'eua', 'moeda', 'norte-americana',
                        'recuou', '0,89%', 'vendida', 'r$', '5,1577', 'veja', 'cotações']
        self.assertEqual(content_raw_to_array(content_raw), response_test)

    def test_count_words(self):
        array_test = ['dólar', 'fechou', 'forte', 'queda', 'nesta', 'segunda-feira',
                        '27', 'dia', 'fraqueza', 'moeda', 'norte-americana', 'exterior',
                        'meio', 'tensões', 'diplomáticas', 'estados', 'unidos', 'china',
                        'investidores', 'modo', 'espera', 'antes', 'reunião', 'política',
                        'monetária', 'federal', 'reserve', 'bc', 'eua', 'moeda', 'norte-americana',
                        'recuou', '0,89%', 'vendida', 'r$', '5,1577', 'veja', 'cotações']
        dictionary_test = {'dólar' : 1, 'fechou' : 1, 'forte' : 1, 'queda' : 1, 'nesta' : 1,
                        'segunda-feira' : 1, '27' : 1, 'dia' : 1, 'fraqueza' : 1, 'moeda': 2,
                        'norte-americana': 2, 'exterior' : 1, 'meio' : 1, 'tensões' : 1,
                        'diplomáticas' : 1, 'estados' : 1, 'unidos' : 1, 'china' : 1, 'investidores' : 1,
                        'modo' : 1, 'espera' : 1, 'antes' : 1, 'reunião' : 1, 'política' : 1, 'monetária' : 1,
                        'federal' : 1, 'reserve' : 1, 'bc' : 1, 'eua' : 1, 'recuou' : 1, '0,89%' : 1, 'vendida' : 1,
                        'r$' : 1, '5,1577' : 1, 'veja' : 1, 'cotações' : 1}
        self.assertDictEqual(count_words(array_test), dictionary_test)

    def test_rank_words(self):
        dictionary_test = {'dólar' : 1, 'fechou' : 1, 'forte' : 1, 'queda' : 1, 'nesta' : 1,
                        'segunda-feira' : 1, '27' : 1, 'dia' : 1, 'fraqueza' : 1, 'moeda': 2,
                        'norte-americana': 2, 'exterior' : 1, 'meio' : 1, 'tensões' : 1,
                        'diplomáticas' : 1, 'estados' : 1, 'unidos' : 1, 'china' : 1, 'investidores' : 1,
                        'modo' : 1, 'espera' : 1, 'antes' : 1, 'reunião' : 1, 'política' : 1, 'monetária' : 1,
                        'federal' : 1, 'reserve' : 1, 'bc' : 1, 'eua' : 1, 'recuou' : 1, '0,89%' : 1, 'vendida' : 1,
                        'r$' : 1, '5,1577' : 1, 'veja' : 1, 'cotações' : 1}
        rank_test = [('moeda', 2), ('norte-americana', 2), ('dólar' , 1), ('fechou' , 1), ('forte' , 1), ('queda' , 1),
                    ('nesta' , 1), ('segunda-feira' , 1), ('27' , 1), ('dia' , 1), ('fraqueza' , 1), ('exterior' , 1),
                    ('meio' , 1), ('tensões' , 1), ('diplomáticas' , 1), ('estados' , 1), ('unidos' , 1), ('china' , 1),
                    ('investidores' , 1), ('modo' , 1), ('espera' , 1), ('antes' , 1), ('reunião' , 1), ('política' , 1),
                    ('monetária' , 1), ('federal' , 1), ('reserve' , 1), ('bc' , 1), ('eua' , 1), ('recuou' , 1), ('0,89%' , 1),
                    ('vendida' , 1), ('r$' , 1), ('5,1577' , 1), ('veja' , 1), ('cotações' , 1)]
        self.assertEqual(rank_words(dictionary_test), rank_test)