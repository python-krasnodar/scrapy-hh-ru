# -*- coding: utf-8 -*-
from urllib.parse import urlencode
import scrapy
from scrapyhhru.items import ResumeItem
from scrapyhhru.settings import HH_RU_MAX_PAGE


class ResumesSpider(scrapy.Spider):
    name = "resumes"
    allowed_domains = ["hh.ru"]
    start_urls = ['https://hh.ru/search/resume?page=%s' % page for page in range(0, HH_RU_MAX_PAGE)]

    def __init__(self, name=None, **kwargs):
        if len(kwargs) != 0:
            start_url_tpl = 'https://hh.ru/search/resume?%s&' % urlencode(kwargs)
        else:
            start_url_tpl = 'https://hh.ru/search/resume?'
        start_url_tpl += 'page={0}'
        self.start_urls = list()
        for page in range(0, HH_RU_MAX_PAGE):
            self.start_urls.append(start_url_tpl.format(page))

        super().__init__(name, **kwargs)

    def parse(self, response):
        for item in response.css('td.output__main-cell'):
            resume = ResumeItem()
            resume['title'] = item.css('.output__name::text').extract_first()
            resume['experience'] = item.css('.output__experience-sum::text').extract_first()
            yield resume
