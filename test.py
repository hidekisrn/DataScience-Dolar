from unittest import TestCase, mock
from bs4 import BeautifulSoup as soup
from NewsParser import NewsParser

class TestScrapping(TestCase):

    def test_get_news(self):
        news_parser = NewsParser(url='https://g1.globo.com/economia/noticia/2020/07/27/dolar.ghtml')
        response = news_parser.get_news()
        self.assertIsInstance(response, list)

    @mock.patch('NewsParser.NewsParser.get_news')
    def test_content_raw_to_phrases(self, mock_get_news):
        data = open('html_test.html', 'r')
        mock_get_news.return_value = soup(data, 'html.parser').findAll('p', {'class': 'content-text__container'})
        news_parser = NewsParser(url='fake_one')
        response_test = [' o dólar fechou em forte queda nesta segunda-feira 27 em dia de fraqueza da moeda norte-americana no exterior em meio às tensões diplomáticas entre estados unidos e china com os investidores em modo de espera antes da reunião de política monetária do federal reserve bc dos eua',
                        ' a moeda norte-americana recuou 0,89% vendida a r$ 5,1577', 'veja mais cotações']
        self.assertEqual(news_parser.content_raw_to_phrases(), response_test)
    
    def test_phrase_to_words(self):
        news_parser = NewsParser(url='fake_one')
        phrase_test = ' o dólar fechou em forte queda nesta segunda-feira 27 em dia de fraqueza da moeda norte-americana no exterior em meio às tensões diplomáticas entre estados unidos e china com os investidores em modo de espera antes da reunião de política monetária do federal reserve bc dos eua'
        word_array_test = ['dólar', 'fechou', 'forte', 'queda', 'nesta', 'segunda-feira', '27',
                           'dia', 'fraqueza', 'moeda', 'norte-americana', 'exterior', 'meio', 'tensões', 'diplomáticas',
                           'estados', 'unidos', 'china', 'investidores', 'modo', 'espera', 'antes', 'reunião', 'política',
                           'monetária', 'federal', 'reserve', 'bc', 'eua']
        self.assertEqual(news_parser.phrase_to_words(phrase_test), word_array_test)

    @mock.patch('NewsParser.NewsParser.content_raw_to_phrases')
    def test_generate_phrases_array(self, mock_content_raw_to_phrases):
        news_parser = NewsParser(url='fake_one')
        mock_content_raw_to_phrases.return_value = [' o dólar fechou em forte queda nesta segunda-feira 27 em dia de fraqueza da moeda norte-americana no exterior em meio às tensões diplomáticas entre estados unidos e china com os investidores em modo de espera antes da reunião de política monetária do federal reserve bc dos eua',
                        ' a moeda norte-americana recuou 0,89% vendida a r$ 5,1577', 'veja mais cotações']
        phrases_array_test = [['dólar', 'fechou', 'forte', 'queda', 'nesta', 'segunda-feira', '27',
                                'dia', 'fraqueza', 'moeda', 'norte-americana', 'exterior', 'meio', 'tensões', 'diplomáticas',
                                'estados', 'unidos', 'china', 'investidores', 'modo', 'espera', 'antes', 'reunião', 'política',
                                'monetária', 'federal', 'reserve', 'bc', 'eua'], ['moeda', 'norte-americana', 'recuou', '0,89%',
                                'vendida', 'r$', '5,1577'], ['veja', 'cotações']]
        self.assertEqual(news_parser.generate_phrases_array(), phrases_array_test)

    @mock.patch('NewsParser.NewsParser.generate_phrases_array')
    def test_count_words(self, mock_generate_phrases_array):
        news_parser = NewsParser(url='fake_one')
        mock_generate_phrases_array.return_value = [['dólar', 'fechou', 'forte', 'queda', 'nesta', 'segunda-feira', '27',
                       'dia', 'fraqueza', 'moeda', 'norte-americana', 'exterior', 'meio', 'tensões', 'diplomáticas',
                       'estados', 'unidos', 'china', 'investidores', 'modo', 'espera', 'antes', 'reunião', 'política',
                       'monetária', 'federal', 'reserve', 'bc', 'eua'], ['moeda', 'norte-americana', 'recuou', '0,89%',
                       'vendida', 'r$', '5,1577'], ['veja', 'cotações']]
        dictionary_test = {'dólar' : 1, 'fechou' : 1, 'forte' : 1, 'queda' : 1, 'nesta' : 1,
                           'segunda-feira' : 1, '27' : 1, 'dia' : 1, 'fraqueza' : 1, 'moeda': 2,
                           'norte-americana': 2, 'exterior' : 1, 'meio' : 1, 'tensões' : 1,
                           'diplomáticas' : 1, 'estados' : 1, 'unidos' : 1, 'china' : 1, 'investidores' : 1,
                           'modo' : 1, 'espera' : 1, 'antes' : 1, 'reunião' : 1, 'política' : 1, 'monetária' : 1,
                           'federal' : 1, 'reserve' : 1, 'bc' : 1, 'eua' : 1, 'recuou' : 1, '0,89%' : 1, 'vendida' : 1,
                           'r$' : 1, '5,1577' : 1, 'veja' : 1, 'cotações' : 1}
        self.assertDictEqual(news_parser.count_words(), dictionary_test)

    @mock.patch('NewsParser.NewsParser.count_words')
    def test_rank_words(self, mock_count_words):
        news_parser = NewsParser(url='fake_one')
        mock_count_words.return_value = {'dólar' : 1, 'fechou' : 1, 'forte' : 1, 'queda' : 1, 'nesta' : 1,
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
        self.assertEqual(news_parser.rank_words(), rank_test)