# -*- coding: utf-8 -*-
import re
from datetime import datetime
import scrapy
from BaseTemp.items import HcUrlItem
from BaseTemp.tools import header_list


class CreditmanageSpider(scrapy.Spider):
    name = 'creditmanage'
    allowed_domains = ['credit-manage.com']
    start_urls = ['http://credit-manage.com/']
    headers = header_list.get_header()

    custom_settings = {
        # do not needs login project
        'COOKIES_ENABLED': False,
        'RETRY_HTTP_CODES': [500, 503, 504, 400, 403, 404, 408],
        'RETRY_TIMES': 1000,
        'DOWNLOAD_DELAY': 0.3,
        'ITEM_PIPELINES': {
            'BaseTemp.pipelines.MongoPipeline': 300,
        },
        # do not needs login project
        'DOWNLOADER_MIDDLEWARES': {
            'BaseTemp.middlewares.UserAgentMiddleware': 200,
            # 'BaseTemp.middlewares.ProxyMiddleware': 10,
        },
        'MONGO_DB': 'creditmanage',
        # 'JOBDIR': 'info/hc360/002',
    }

    def parse(self, response):
        # 发起请求
        yield scrapy.FormRequest(
            url='http://credit-manage.com/search.htm',
            formdata={'condition':'杨勇'},
            callback = self.parse_page,
            headers=self.headers
        )

    def parse_page(self,response):
        print(response.text)
        pass
