# -*- coding: utf-8 -*-
import scrapy


class VacanciesSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = ["hh.ru"]
    start_urls = (
        'http://www.hh.ru/',
    )

    def parse(self, response):
        pass
