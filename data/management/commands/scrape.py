from django.core.management.base import BaseCommand, CommandError
from scrapy.crawler import CrawlerProcess

from my_project.crawler.spiders.spider import  QuotesSpider

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        process = CrawlerProcess()
        process.crawl(QuotesSpider)
        process.start()