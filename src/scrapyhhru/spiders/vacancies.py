# -*- coding: utf-8 -*-
import scrapy
from scrapyhhru.items import VacancyItem
from scrapyhhru.settings import HH_RU_MAX_PAGE


class VacanciesSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = ["hh.ru"]
    start_urls = ['https://hh.ru/search/vacancy?page=%s' % page for page in range(0, HH_RU_MAX_PAGE)]

    def parse(self, response):
        for item in response.css('.search-result-item'):
            vacancy = VacancyItem()
            vacancy['title'] = item.css('.search-result-item__name::text').extract_first()
            vacancy['description'] = item.css('.search-result-item__snippet::text').extract_first()
            yield vacancy
