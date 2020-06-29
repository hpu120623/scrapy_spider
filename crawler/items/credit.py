from .base import *


# 舆情数据字段
class CreditItem(BaseItem):
    status = scrapy.Field()             # 请求状态
    area = scrapy.Field()               # 区域
    found_time = scrapy.Field()         # 创建时间
    legal_person = scrapy.Field()       # 法人
    interface = scrapy.Field()          # 请求接口
    spider = scrapy.Field()             # 表格名称