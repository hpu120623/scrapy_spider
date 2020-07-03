import re
import json
from pprint import pprint

from scrapy import Spider, Request, FormRequest

from .notcie_config import *
from crawler.captcha_ocr import BaiDuOCR, OtherOCR


class ChinataxMissNoticeSpider(Spider):
    name = 'chinatax_miss_notice'
    true = ''
    code = ''
    test_code = 130000

    headers = {
        # 'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }

    def start_requests(self):
        if self.test_code in area_dict:
            task = area_dict[self.test_code]
            if self.test_code == 110000 or self.test_code == 370000 or self.test_code == 230000 or self.test_code == 350200 \
                    or self.test_code == 450000:
                yield FormRequest(task['detail_url'], formdata=task['data'], callback=self.parse_detail, meta={'task': task})
            elif self.test_code == 530000:
                yield Request(task['detail_url'], callback=self.parse_detail, meta={'task': task})
            else:
                yield Request(task['request_url'], headers=self.headers, callback=self.parse_captcha, meta={'task': task})
        else:
            self.logger.info(f'Area Is Error...')

    def parse_captcha(self, response):
        self.logger.info(f'Parse Captcha: {response.url}')

        token = ''
        _csrf = ''
        task = response.meta['task']

        if self.test_code == 130000:
            with open('captcha.jpg', 'wb') as f:
                f.write(response.body)

            captcha_text = OtherOCR().parse_captcha('captcha.jpg')
            print(f'captcha_text: {captcha_text}')

            if 'yzm' in task['captcha_data']:
                task['captcha_data']['yzm'] = captcha_text
            elif 'checknum' in task['captcha_data']:
                task['captcha_data']['checknum'] = captcha_text
    #
            yield FormRequest(task['captcha_url'], formdata=task['captcha_data'], callback=self.parse_data,headers=self.headers,
                              meta={'task': task, 'token': token, 'yzm': captcha_text})
        else:
            if self.test_code == 120000:
                token = re.findall(r'.*token" value="(.*?)"', response.text)[0]
            elif self.test_code == 430000:
                _csrf = re.findall(r'name="_csrf" content=\"(.*?)\"/>', response.text)[0]
            yield Request(task['captcha_url'], headers=self.headers, callback=self.parse_data, meta={'task': task, 'token': token, 'csrf': _csrf})

    def parse_data(self, response):
    #     self.logger.info(f'Parse Data: {response.url}')
    #
        task = response.meta['task']
        token = response.meta['token']
    #
        if self.test_code == 130000:
            task['data']['yzm'] = response.meta['yzm']
            yield FormRequest(task['detail_url'], formdata=task['data'], headers=self.headers, callback=self.parse_detail,
                              meta={'task': task, 'detail': 1})
        else:
            with open("captcha.jpg", 'wb') as f:
                f.write(response.body)

            if self.test_code == 120000 or self.test_code == 430000:
                captcha_text = OtherOCR().parse_captcha('captcha.jpg')
            else:
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
                elif 'jym' in task['data']:
                    task['data']['jym'] = captcha_text
                elif 'captcha' in task['data']:
                    task['data']['captcha'] = captcha_text
                elif 'code' in task['data']:
                    task['data']['code'] = captcha_text
                elif 'ipt_xm' in task['data']:
                    task['data']['ipt_xm'] = captcha_text
                elif 'token' in task['data']:
                    task['data']['token'] = token
                elif '_csrf' in task['data']:
                    task['data']['_csrf'] = response.meta.get('_csrf')
                yield FormRequest(task['detail_url'], formdata=task['data'], headers=self.headers, callback=self.parse_detail, meta={'task': task})
    #
    def parse_detail(self, response):
        self.logger.info(f'Parse Detail: {response.url}')

        count = 0
        false = ''
        task = response.meta['task']
        try:
            if task['type'] == 'html':
                if self.test_code == 230000:
                    count = len(response.css('table#dzswj_bb tr')[2:])
                elif self.test_code == 370200:
                    count = len(response.css('.table-scrollable-horizontal tbody.text-dark').extract())
                elif self.test_code == 460000:
                    count = len(response.css('.list_table tr'))
            else:
                text = response.text
                result = json.loads(text)
                if self.test_code == 110000:
                    count = eval(result['json'])['data'][0]['resultList']
                elif self.test_code == 370000:
                    count = result['message']['totalPage']
                elif self.test_code == 530000:
                    count = len(result['resultObj'])
                elif self.test_code == 350200:
                    count = result['total']
                elif self.test_code == 450000:
                    pprint(result['data'])
        except Exception as e:
            count = 0
            print(f'Error: {e}')
        finally:
            print(f'count: {count}')