import re
import json
import time
from pprint import pprint

from scrapy import Spider, Request, FormRequest

from .payer_status_config import *
from crawler.captcha_ocr import BaiDuOCR, OtherOCR


class ChinataxPayerStatusSpider(Spider):
    name = 'chinatax_payer_status'
    true = ''
    code = ''
    test_code = 510000

    headers = {
        # 'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }

    def start_requests(self):
        if self.test_code in area_dict:
            task = area_dict[self.test_code]
            if self.test_code == 370000:
                yield FormRequest(task['detail_url'], formdata=task['data'], callback=self.parse_detail,
                                  meta={'task': task})
            elif self.test_code == 650000:
                detail_url = task['detail_url'].format(company_code='916501055643558439')
                yield Request(detail_url, callback=self.parse_detail, meta={'task': task})
            else:
                yield Request(task['request_url'], callback=self.parse_captcha, meta={'task': task})
        else:
            self.logger.info(f'Area Is Error...')

    def parse_captcha(self, response):
        self.logger.info(f'Parse Captcha: {response.url}')

        token = ''
        _csrf = ''
        task = response.meta['task']

        if self.test_code == 120000:
            token = re.findall(r'.*token" value="(.*?)"', response.text)[0]
        elif self.test_code == 430000:
            _csrf = re.findall(r'.*_csrf" value="(.*?)"', response.text)[0]
        yield Request(task['captcha_url'], callback=self.parse_data, meta={'task': task, 'token': token, 'csrf': _csrf})

    def parse_data(self, response):
        self.logger.info(f'Parse Data: {response.url}')

        task = response.meta['task']
        token = response.meta.get('token', '')
        csrf = response.meta.get('csrf', '')

        with open("captcha.jpg", 'wb') as f:
            f.write(response.body)

        if self.test_code == 130000 or self.test_code == 310000 or self.test_code == 330000 or \
                self.test_code == 410000 or self.test_code == 430000 or self.test_code == 440000 or \
                self.test_code == 460000 or self.test_code == 500000 or self.test_code == 530000 or \
                self.test_code == 620000 or self.test_code == 630000 or self.test_code == 640000 or \
                self.test_code == 330200 or self.test_code == 370200 or self.test_code == 510000:
            captcha_text = OtherOCR().parse_captcha('captcha.jpg')
        else:
            captcha_text = BaiDuOCR().parse_captcha('captcha.jpg')
        self.logger.info(f'captcha_text: {captcha_text}')

        if task['method'] == 'get':
            if self.test_code == 440000 or self.test_code == 630000:
                task['bw']['taxML']['body']['captcha'] = captcha_text
                detail_url = task['detail_url'] + quote(str(task['bw']))
                yield Request(detail_url, callback=self.parse_detail, meta={'task': task, 'detail': 1})
            elif self.test_code == 130000:
                task['data']['yzm'] = captcha_text
                yield Request(task['detail_url'], method='POST', body=json.dumps(task['data']), headers=self.headers, callback=self.parse_detail, meta={'task': task})
            elif self.test_code == 330000 or self.test_code == 410000:
                detail_url = task['detail_url'].format(captcha_code=captcha_text)
                yield Request(detail_url, callback=self.parse_detail, meta={'task': task})
            elif self.test_code == 620000:
                task['data']['verifyCode'] = captcha_text
                self.headers['Content-Type'] = 'application/json;charset=UTF-8'
                yield Request(task['detail_url'], method='POST', body=json.dumps(task['data']), headers=self.headers, callback=self.parse_detail, meta={'task': task})
            elif self.test_code == 330200 or self.test_code == 510000:
                task['data']['yzm'] = captcha_text
                self.headers['Content-Type'] = 'application/json;charset=UTF-8'
                yield Request(task['detail_url'], method='POST', body=json.dumps(task['data']), headers=self.headers, callback=self.parse_detail, meta={'task': task})
            elif self.test_code == 370200:
                detail_url = task['detail_url'].format(captcha_code=captcha_text, company_code='913702007137253437')
                yield Request(detail_url, callback=self.parse_detail, meta={'task': task})
            else:
                detail_url = task['detail_url'].format(captcha_code=captcha_text)
                yield Request(detail_url, callback=self.parse_detail, meta={'task': task, 'detail': 1})
        else:
            detail_url = task['detail_url']
            if self.test_code == 120000:
                task['data']['jym'] = captcha_text
                task['data']['token'] = token
            if self.test_code == 310000:
                task['data']['yzm'] = captcha_text
                self.headers['Content-Type'] = 'application/json;charset=UTF-8'
            elif self.test_code == 360000:
                task['data']['yzm'] = captcha_text
            elif self.test_code == 430000:
                task['data']['yzm'] = captcha_text
                task['data']['_csrf'] = csrf
            elif self.test_code == 460000:
                task['data']['captcha'] = captcha_text
            elif self.test_code == 500000:
                task['bw']['identifyCode'] = captcha_text
                detail_url = task['detail_url'] + str(task['bw'])
            elif self.test_code == 530000:
                task['data']['randCode'] = captcha_text
            elif self.test_code == 640000:
                task['data']['yzm'] = captcha_text
                self.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
            yield FormRequest(detail_url, formdata=task['data'], headers=self.headers, callback=self.parse_detail, meta={'task': task})

    def parse_detail(self, response):
        self.logger.info(f'Parse Detail: {response.url}')

        count = 0
        task = response.meta['task']
        try:
            if task['type'] == 'html':
                print(response.text)
                if self.test_code == 120000:
                    count = len(response.css('#text tbody:nth-child(2) tr'))
                elif self.test_code == 460000:
                    count = len(response.css('.list_table tbody tr'))
                elif self.test_code == 2222:
                    count = len(response.css('.list_table tr'))
            else:
                text = response.text
                result = json.loads(text)
                if self.test_code == 110000:
                    count = len(result['arrayList'])
                elif self.test_code == 370000:
                    count = len(result['message'])
                elif self.test_code == 130000:
                    count = len(result['value'])
                elif self.test_code == 330000:
                    count = len(result['resultObj'])
                elif self.test_code == 360000:
                    count = len(result['reData']['resultInfo'])
                elif self.test_code == 410000:
                    data_list = result['data']
                    if data_list:
                        for data in data_list:
                            if '非正常' in data['NSRZT']:
                                count += 1
                elif self.test_code == 430000:
                    data_list = result['data']
                    if data_list:
                        for data in data_list:
                            if '非正常' in data['djzt']:
                                count += 1
                elif self.test_code == 440000:
                    pass
                elif self.test_code == 500000:
                    pass
                elif self.test_code == 530000:
                    for data in result:
                        if '非正常' in data['nsrzt_mc']:
                            count += 1
                elif self.test_code == 620000:
                    data_list = result['data']
                    if data_list:
                        for data in data_list:
                            if '是' in data['sffzch']:
                                count += 1
                elif self.test_code == 330200 or self.test_code == 510000:
                    data_list = result['value']
                    if data_list:
                        for data in data_list:
                            if '非正常' in data['nsrztmc']:
                                count += 1
                elif  self.test_code == 650000:
                    data_list = result['value']
                    if data_list:
                        for data in data_list:
                            if '非正常' in data['nsrzt']:
                                count += 1
                pprint(result)
        except Exception as e:
            count = 0
            print(f'Error: {e}')
        finally:
            print(f'count: {count}')
