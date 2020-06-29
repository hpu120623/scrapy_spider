from .base import *


# 舆情数据字段
class OpinionItem(BaseItem):
    type = scrapy.Field()               # 一级分类
    html = scrapy.Field()               # response.text
    theme = scrapy.Field()              # 二级分类
    count = scrapy.Field()              # 关键词次数
    source = scrapy.Field()             # 来源
    search_count = scrapy.Field()       # 搜索次数
    company_tag = scrapy.Field()        # 公司标签
    company_name = scrapy.Field()       # 公司名称