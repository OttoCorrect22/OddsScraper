import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote-spider'
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        QUOTE_SELECOR = '.quote'
        TEXT_SELECOR = '.text::text'
        AUTHOR_SELECOR = '.author::text'
        ABOUT_SELECTOR = '.author + a::attr("href")'
        TAGS_SELECTOR = '.tags > .tag::text'

        for quote in response.css(QUOTE_SELECOR):
            pass