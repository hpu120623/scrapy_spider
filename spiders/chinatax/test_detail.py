import json

from scrapy import Spider, FormRequest, Request


class SpiderDetail(Spider):
    name = 'test_detail'

    def start_requests(self):
        request_api = 'https://etax.hebei.chinatax.gov.cn/yhs-web/api/nsrzg/query/nsrztcx'
        form_data = {
            'shxydm': '911304045700544144',
            'nsrmc': '河北智贞钢铁贸易有限公司',
            'yzm': '2323'
        }
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',

        }
        yield FormRequest(request_api, formdata=form_data, headers=headers, callback=self.parse)

    def parse(self, response):

        print(json.loads(response.text))