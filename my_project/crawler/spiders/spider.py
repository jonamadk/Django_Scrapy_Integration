import scrapy
# from datetime import date
from my_project.crawler.items import CrawlerItem
from data.models import LiveTradingData

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://merolagani.com/LatestMarket.aspx',

    ]

    def parse(self, response):
      
        for data in response.xpath('//*[@class="table-responsive"]//tbody//tr'):
            company_name_symbol = data.xpath('td[1]//text()').extract_first()
            change_percent_value= data.xpath('td[4]/text()').extract_first()
            high_value = data.xpath('td[5]//text()').extract_first()
            low_value = data.xpath('td[6]//text()').extract_first()
            open_value = data.xpath('td[7]//text()').extract_first()
            qty= data.xpath('td[8]//text()').extract_first()
            

            item = LiveTradingData(company_name_symbol=company_name_symbol,high_value = float(high_value.replace(',','')), low_value= float(low_value.replace(',','')),
                        open_value= float(open_value.replace(',','')), qty= float(qty.replace(',','')),
                        change_percent_value = float(change_percent_value.replace(',','')))

            item.save()


            
        
          
       


    