import time

import scrapy

__all__ = ['BaseItem', 'scrapy']


# 基础数据字段
# TODO 与产品、后端核定各数据字段
class BaseItem(scrapy.Item):
    key = scrapy.Field()            # redis key
    batch = scrapy.Field()          # 批次数
    uuid = scrapy.Field()           # 平台唯一ID
    type = scrapy.Field()           # 类型
    url = scrapy.Field()            # 访问URL
    company_code = scrapy.Field()   # 信用代码
    company_name = scrapy.Field()   # 公司名称
    publish_time = scrapy.Field()   # 发布时间

    def __init__(self):
        super().__init__()
        self['fetchTime'] = int(time.time() * 1000)
