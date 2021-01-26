import scrapy

from my_project.crawler.items import CrawlerItem
from data.models import Data

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',

    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            title = quote.css('span.text::text').get()
            item = Data(title=title)
            item.save()
            yield{
            'title': quote.css('span.text::text').get()
            
            }
         
          
       


    