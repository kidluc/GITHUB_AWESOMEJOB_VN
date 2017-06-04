# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import time
from scrapy.item import Item, Field


class Items(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    link = Field()
    content = Field()

    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    pass


def time_conver(n):
    ''' Convert string time to ISO format '''
    convert = time.strftime(n, "%A, %d %B %Y")
    return time.strftime("%Y-%m-%d", convert)

def rm(L, i):
    while i in L:
        L.remove(i)
    return L