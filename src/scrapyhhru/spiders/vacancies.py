# -*- coding: utf-8 -*-
from urllib.parse import urlencode
import scrapy
from scrapyhhru.items import VacancyItem
from scrapyhhru.settings import HH_RU_MAX_PAGE


class VacanciesSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = ["hh.ru"]
    start_urls = ['https://hh.ru/search/vacancy?page=%s' % page for page in range(0, HH_RU_MAX_PAGE)]

    def __init__(self, name=None, **kwargs):
        if len(kwargs) != 0:
            start_url_tpl = 'https://hh.ru/search/vacancy?%s&' % urlencode(kwargs)
        else:
            start_url_tpl = 'https://hh.ru/search/vacancy?'
        start_url_tpl += 'page={0}'
        self.start_urls = list()
        for page in range(0, HH_RU_MAX_PAGE):
            self.start_urls.append(start_url_tpl.format(page))

        super().__init__(name, **kwargs)

    def parse(self, response):
        for item in response.css('.search-result-item'):
            vacancy = VacancyItem()
            vacancy['title'] = item.css('.search-result-item__name::text').extract_first()
            vacancy['description'] = item.css('.search-result-item__snippet::text').extract_first()
            yield vacancy
