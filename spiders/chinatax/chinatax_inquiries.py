import re
import json
import time
from pprint import pprint

import muggle_ocr

from scrapy import Spider, Request, FormRequest

from .company_config import *
from crawler.captcha_ocr import BaiDuOCR, OtherOCR


class ChinataxInquiriesSpider(Spider):
    name = 'chinatax_inquiries'
    true = ''
    code = ''
    test_code = 530000
    
    def start_requests(self):
        if self.test_code in area_dict:
            task = area_dict[self.test_code]
            if self.test_code == 230000 or self.test_code == 310000:
                yield FormRequest(task['detail_url'], formdata=task['data'], callback=self.parse_detail, meta={'task': task})
            elif self.test_code == 530000:
                yield Request(task['detail_url'], callback=self.parse_detail, meta={'task': task, 'detail': 1})
            else:
                yield Request(task['request_url'], callback=self.parse_captcha, meta={'task': task})
        else:
            self.logger.info(f'Area Is Error...')

    def parse_captcha(self, response):
        self.logger.info(f'Parse Captcha: {response.url}')

        task = response.meta['task']
        if self.test_code == 420000 or self.test_code == 620000 or self.test_code == 650000:
            with open('captcha.jpg', 'wb') as f:
                f.write(response.body)

            captcha_text = OtherOCR().parse_captcha('captcha.jpg')
            print(f'captcha_text: {captcha_text}')

            if 'yzm' in task['captcha_data']:
                task['captcha_data']['yzm'] = captcha_text
            elif 'checknum' in task['captcha_data']:
                task['captcha_data']['checknum'] = captcha_text

            yield FormRequest(task['captcha_url'], formdata=task['captcha_data'], callback=self.parse_data, meta={'task': task, 'yzm': captcha_text})
        # elif self.test_code == 530000:
        #     with open('captcha.jpg', 'wb') as f:
        #         f.write(response.body)
        #
        #     captcha_text = BaiDuOCR().parse_captcha('captcha.jpg')
        #     check_captcha = task['captcha_url'].format(captcha_code=captcha_text)
        #     yield Request(check_captcha, callback=self.parse_data, meta={'task': task})
        else:
            now_time = response.meta.get('now_time', '')
            captcha_url = task['captcha_url'].format(time=now_time) if now_time else task['captcha_url']
            yield Request(captcha_url, callback=self.parse_data, meta={'task': task})

    def parse_data(self, response):
        self.logger.info(f'Parse Data: {response.url}')

        task = response.meta['task']

        if self.test_code == 420000 or self.test_code == 620000 or self.test_code == 650000:
            print(response.text)
            if response.meta.get('yzm'):
                task['data']['yzm'] = response.meta['yzm']
            yield FormRequest(task['detail_url'], formdata=task['data'], callback=self.parse_detail, meta={'task':task, 'detail': 1})
        # elif self.test_code == 530000:
        #     yield Request(task['detail_url'], callback=self.parse_detail, meta={'task': task, 'detail': 1})
        else:
            with open("captcha.jpg",'wb') as f:
                f.write(response.body)
            # 河南的验证码调用百度ocr识别率很低
            if self.test_code == 410000 or self.test_code == 450000 or self.test_code == 460000:
                captcha_text = OtherOCR().parse_captcha('captcha.jpg')
            else:
                # captcha_text = OtherOCR().parse_captcha('captcha.jpg')
                captcha_text = BaiDuOCR().parse_captcha('captcha.jpg')
            print(f'captcha_text: {captcha_text}')

            if task['method'] == 'get':
                if self.test_code == 440000 or self.test_code == 520000 or self.test_code == 630000:
                    task['bw']['taxML']['body']['captcha'] = captcha_text
                    detail_url = task['detail_url'] + str(task['bw'])
                    yield Request(detail_url, callback=self.parse_detail, meta={'task': task, 'detail': 1})
                else:
                    detail_url = task['detail_url'].format(captcha_code=captcha_text)
                    yield Request(detail_url, callback=self.parse_detail, meta={'task': task, 'detail': 1})
            else:
                if 'yzm' in task['data']:
                    task['data']['yzm'] = captcha_text
                elif 'rcode' in task['data']:
                    task['data']['rcode'] = captcha_text
                elif 'captcha' in task['data']:
                    task['data']['captcha'] = captcha_text
                elif 'code' in task['data']:
                    task['data']['code'] = captcha_text
                yield FormRequest(task['detail_url'], formdata=task['data'], callback=self.parse_detail, meta={'task': task, 'detail': 1})

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
                    if '未查询到' in first_text:
                        count = 0
                    else:
                        count = len(result)
                elif self.test_code == 460000:
                    count = len(response.css('.list_table tr'))
            else:
                text = response.text
                if self.test_code == 410000:
                    text = re.findall(r'\((.*)\)', response.text)[0]
                result = json.loads(text)
                if self.test_code == 220000:
                    count = result['data'][1]['value']
                elif self.test_code == 320000:
                    count = len(result['DATA'].get('qsxxList', []))
                elif self.test_code == 330000:
                    count = len(result.get('resultObj', []))
                elif self.test_code == 340000:
                    count = result['data']['list'].get('total', 0)
                elif self.test_code == 410000:
                    count = len(result.get('data', []))
                elif self.test_code == 420000:
                    count = len(result.get('data', []))
                elif self.test_code == 440000 or self.test_code == 520000 or self.test_code == 630000:
                    count = len(result['taxML']['body']['taxML']['qsqyList'].get('qsqy', []))
                elif self.test_code == 450000:
                    count = len(result.get('data', []))
                elif self.test_code == 530000:
                    count = len(result.get('resultObj', []))
                pprint(result)
        except Exception as e:
            count = 0
            print(f'Error: {e}')
        finally:
            print(f'count: {count}')
