import re
import json

from pprint import pprint

from scrapy import Spider, Request, FormRequest

from .inquires_config import *
from crawler.captcha_ocr import BaiDuOCR, OtherOCR


# 021-企业在国税平台是否存在欠税情况
class ChinataxInquiriesSpider(Spider):
    name = 'chinatax_inquiries'
    true = ''
    code = ''
    test_code = 650000

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }

    def start_requests(self):
        if self.test_code in area_dict:
            task = area_dict[self.test_code]
            if self.test_code == 230000 or self.test_code == 420000:
                yield FormRequest(task['detail_url'], formdata=task['data'], callback=self.parse_detail,
                                  meta={'task': task})
            elif self.test_code == 530000:
                yield Request(task['detail_url'], callback=self.parse_detail, meta={'task': task})
            else:
                yield Request(task['request_url'], callback=self.parse_captcha, meta={'task': task})
        else:
            self.logger.info(f'Area Is Error...')

    def parse_captcha(self, response):
        self.logger.info(f'Request End: {response.url}')

        task = response.meta['task']
        yield Request(task['captcha_url'], callback=self.parse_data, meta={'task': task})

    def parse_data(self, response):
        self.logger.info(f'Parse Captcha: {response.url}')

        task = response.meta['task']

        # 存储验证码
        with open("captcha.jpg", 'wb') as f:
            f.write(response.body)

        # 调用百度ocr识别率很低
        if self.test_code == 220000 or self.test_code == 320000 or self.test_code == 360000 or \
                self.test_code == 370000 or self.test_code == 410000 or self.test_code == 450000 or \
                self.test_code == 460000 or self.test_code == 500000 or self.test_code == 620000 or \
                self.test_code == 650000:
            captcha_text = OtherOCR().parse_captcha('captcha.jpg')
        else:
            captcha_text = BaiDuOCR().parse_captcha('captcha.jpg')
        print(f'captcha_text: {captcha_text}')

        if task['method'] == 'get':
            if self.test_code == 440000 or self.test_code == 520000 or self.test_code == 630000:
                task['bw']['taxML']['body']['captcha'] = captcha_text
                detail_url = task['detail_url'] + str(task['bw'])
                yield Request(detail_url, callback=self.parse_detail, meta={'task': task})
            elif self.test_code == 620000 or self.test_code == 650000:
                task['data']['yzm'] = captcha_text
                self.headers['Content-Type'] = 'application/json;charset=UTF-8'
                yield Request(task['detail_url'], method='POST', body=json.dumps(task['data']), headers=self.headers,
                              meta={'task': task}, callback=self.parse_detail)
            else:
                detail_url = task['detail_url'].format(captcha_code=captcha_text)
                yield Request(detail_url, callback=self.parse_detail, meta={'task': task})
        else:
            if self.test_code == 220000 or self.test_code == 320000 or self.test_code == 340000 or \
                    self.test_code == 360000 or self.test_code == 370000:
                task['data']['yzm'] = captcha_text
            elif self.test_code == 410000 or self.test_code == 450000:
                task['data']['rcode'] = captcha_text
            elif self.test_code == 460000:
                task['data']['captcha'] = captcha_text
            elif self.test_code == 500000:
                task['data']['code'] = captcha_text
            yield FormRequest(task['detail_url'], formdata=task['data'], headers=self.headers, callback=self.parse_detail, meta={'task': task, 'detail': 1})

    def parse_detail(self, response):
        self.logger.info(f'Parse Detail: {response.url}')

        count = 0
        task = response.meta['task']
        try:
            if task['type'] == 'html':
                if self.test_code == 230000:
                    count = len(response.css('table#dzswj_bb tr')[2:])
                elif self.test_code == 370000:
                    result = response.css('table#tb tr')[2:]
                    first_text = result[0].css('::text').extract_first()
                    if '未查询到' not in first_text:
                        count = len(result)
                elif self.test_code == 460000:
                    count = len(response.css('.list_table tr'))
            else:
                if self.test_code == 410000:
                    text = re.findall(r'\((.*)\)', response.text)[0]
                    result = json.loads(text)
                    count = len(result.get('data', []))
                else:
                    result = json.loads(response.text)
                    if self.test_code == 220000:
                        count = result['data'][1]['value']
                    elif self.test_code == 320000:
                        count = len(result['DATA'].get('qsxxList', []))
                    elif self.test_code == 330000:
                        count = len(result.get('resultObj', []))
                    elif self.test_code == 340000:
                        count = result['data']['list'].get('total', 0)
                    elif self.test_code == 420000:
                        count = result.get('count', 0)
                    elif self.test_code == 440000 or self.test_code == 520000 or self.test_code == 630000:
                        count = len(result['taxML']['body']['taxML']['qsqyList'].get('qsqy', []))
                    elif self.test_code == 450000:
                        count = len(result.get('data', []))
                    elif self.test_code == 530000:
                        count = len(result.get('resultObj', []))
                    elif self.test_code == 620000 or self.test_code == 650000:
                        count = result['value'].get('total', 0)
                pprint(result)
        except Exception as e:
            count = 0
            print(f'Error: {e}')
        finally:
            print(f'count: {count}')
