# -*- coding: utf-8 -*-
import scrapy
import logging
# from scrapy.loader import ItemLoader


# class DSChannel(scrapy.Item):
#     channel = scrapy.Field()
#     lock_status = scrapy.Field()
#     modulation = scrapy.Field()
#     channel_ID = scrapy.Field()
#     frequency = scrapy.Field()
#     power = scrapy.Field()
#     snr = scrapy.Field()
#     corrected = scrapy.Field()
#     uncorrectables = scrapy.Field()


class ModemStatusSpider(scrapy.Spider):
    name = 'modem-status'
    allowed_domains = ['192.168.100.1']
    start_urls = ['http://192.168.100.1/RgConnect.asp']

    def parse(self, response):
        ds_rows = response.selector.xpath("//table/tr")
        for row in ds_rows:
            ds_columns = row.xpath(".//td")
            if len(ds_columns) != 9:
                continue
            yield {
                "channel": ds_columns[0].xpath("text()").get(),
                "lock_status": ds_columns[1].xpath("text()").get(),
                "modulation": ds_columns[2].xpath("text()").get(),
                "channel_ID": ds_columns[3].xpath("text()").get(),
                "frequency": ds_columns[4].xpath("text()").get(),
                "power": ds_columns[5].xpath("text()").get(),
                "snr": ds_columns[6].xpath("text()").get(),
                "corrected": ds_columns[7].xpath("text()").get(),
                "uncorrectables": ds_columns[8].xpath("text()").get()
            }
