# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ResumeItem(scrapy.Item):
    title = scrapy.Field()
    experience = scrapy.Field()


class VacancyItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()

