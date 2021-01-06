from NewsParser import NewsParser

def main():
    news_parser = NewsParser("https://g1.globo.com/economia/noticia/2020/07/27/dolar.ghtml")
    #content_news = news_parser.get_news()
    #array_of_phrases = news_parser.content_raw_to_phrases()
    #matrix_of_words = news_parser.generate_phrases_array()
    #count_of_words = news_parser.count_words()
    ranked_words = news_parser.rank_words()

    print(news_parser)
    #print(content_news)
    #print(array_of_phrases)
    #print(matrix_of_words)
    #print(count_of_words)
    print(ranked_words)

if __name__ == "__main__":
    main()