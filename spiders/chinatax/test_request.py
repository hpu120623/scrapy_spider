import re
import json
from pprint import pprint

from scrapy import Spider, FormRequest, Request


class SpiderDetail(Spider):
    name = 'test_request'

    def start_requests(self):
        request_api = 'https://xin.baidu.com/detail/compinfo?pid=xlTM-TogKuTwV-8MPnfHULi59b1VNzNGIwmd'
        form_data = {
            'nsrsbh': '91410322745760055R',
            'yzm': ''
        }
        # headers = {
        #     # 'Content-Type': 'application/json;charset=UTF-8',
        #     # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        #
        # }
        yield Request(request_api, callback=self.parse)

    def parse(self, response):
        print(response.url)
        result = re.findall(r'(\d+)', response.url)[0]
        detail_url = 'https://xin.baidu.com/detail/basicAllDataAjax?pid={}'.format(result)
        yield Request(detail_url, callback=self.parse_detail)

    def parse_detail(self, response):
        self.logger.info(f'Parse Detail: {response.url}')

        result = json.loads(response.text)
        pprint(result)