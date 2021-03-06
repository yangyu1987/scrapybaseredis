# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import pymongo


class BasetempItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #抓取时间
    crawl_time = scrapy.Field()
    # 电影标题
    title = scrapy.Field()
    # 上演时间
    time = scrapy.Field()
    # 出品地区
    area = scrapy.Field()

    mongo_collection = scrapy.Field()

    def mongo_insert(self):

        data = {
            'crawl_time':self['crawl_time'],
            'title': self['title'],
            'time': self['time'],
            'area': self['area'],
        }
        mongo_collection = self['mongo_collection']

        return mongo_collection,data

class PhoneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #抓取时间
    crawl_time = scrapy.Field()
    phone_num = scrapy.Field()
    area = scrapy.Field()
    service_provider = scrapy.Field()

    mongo_collection = scrapy.Field()

    def mongo_insert(self):

        data = {
            'crawl_time':self['crawl_time'],
            'phone_num': self['phone_num'],
            'area': self['area'],
            'service_provider': self['service_provider'],
        }
        mongo_collection = self['mongo_collection']

        return mongo_collection,data

class ChaohaoItem(scrapy.Item):
    # 抓取时间
    crawl_time = scrapy.Field()
    num = scrapy.Field()
    lables = scrapy.Field()

    mongo_collection = scrapy.Field()

    def mongo_insert(self):
        data = {
            'crawl_time': self['crawl_time'],
            'num': self['num'],
            'lables': self['lables'],
        }
        mongo_collection = self['mongo_collection']

        return mongo_collection, data


class HcUrlItem(scrapy.Item):
    # 慧聪网企业网址
    crawl_time = scrapy.Field()
    comp_name = scrapy.Field()
    comp_id = scrapy.Field()
    comp_page = scrapy.Field()

    mongo_collection = scrapy.Field()

    def mongo_insert(self):

        data = {
            'crawl_time':self['crawl_time'],
            'comp_id': self['comp_id'],
            'comp_name': self['comp_name'],
            'comp_page': self['comp_page'],
        }
        mongo_collection = self['mongo_collection']

        return mongo_collection,data
