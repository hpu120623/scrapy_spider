import json
from pprint import pprint
from urllib.parse import quote, urlencode

from scrapy import Spider, FormRequest, Request
from .miss_notice_config import *
from crawler.captcha_ocr import BaiDuOCR


class SpiderDetail(Spider):
    name = 'test_detail'

    def start_requests(self):
        request_api = 'http://shanghai.chinatax.gov.cn/newxbwz/wzfw/YhscxCtrl-yhsCx.pfv'
        form_data = {
            'shhtym': '9131011669293804XG',
            'yzm': ''
        }
        headers = {
            # 'Content-Type': 'application/json;charset=UTF-8',
            # 'Origin': 'https://etax.ningxia.chinatax.gov.cn',
            # 'Referer': 'https://etax.ningxia.chinatax.gov.cn/sword?ctrl=NsrztcxCtrl_initView',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        }
        yield FormRequest(request_api, formdata=form_data, headers=headers, callback=self.parse)
        # yield Request(request_api, method='POST', body=json.dumps(form_data), headers=headers, callback=self.parse)
        # yield Request(request_api, headers=headers, callback=self.parse)

    def parse(self, response):
        print(response.text)
        # pprint(json.loads(response.text))