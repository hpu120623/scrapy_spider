import re
import json
from pprint import pprint

from scrapy import Spider, Request, FormRequest

from .miss_notice_config import *
from crawler.captcha_ocr import BaiDuOCR, OtherOCR


class ChinataxMissNoticeSpider(Spider):
    name = 'chinatax_miss_notice'
    true = ''
    code = ''
    test_code = 130000

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }

    def start_requests(self):
        if self.test_code in area_dict:
            task = area_dict[self.test_code]
            if self.test_code == 110000 or self.test_code == 230000 or self.test_code == 350200 or \
                    self.test_code == 370000  or self.test_code == 450000:
                yield FormRequest(task['detail_url'], formdata=task['data'], callback=self.parse_detail, meta={'task': task})
            elif self.test_code == 440000:
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

        if self.test_code == 120000:
            token = re.findall(r'.*token" value="(.*?)"', response.text)[0]
        elif self.test_code == 430000:
            _csrf = re.findall(r'name="_csrf" content=\"(.*?)\"/>', response.text)[0]
        yield Request(task['captcha_url'], headers=self.headers, callback=self.parse_data, meta={'task': task, 'token': token, 'csrf': _csrf})

    def parse_data(self, response):
        self.logger.info(f'Parse Data: {response.url}')

        task = response.meta['task']
        token = response.meta['token']

        with open("captcha.jpg", 'wb') as f:
            f.write(response.body)

        if self.test_code == 130000 or self.test_code == 430000 or self.test_code == 640000:
            captcha_text = OtherOCR().parse_captcha('captcha.jpg')
        else:
            captcha_text = BaiDuOCR().parse_captcha('captcha.jpg')
        print(f'captcha_text: {captcha_text}')

        if task['method'] == 'get':
            if self.test_code == 130000 or self.test_code == 430000:
                task['data']['yzm'] = captcha_text
                self.headers['Content-Type'] = 'application/json;charset=UTF-8'
                yield Request(task['detail_url'], method='POST', body=json.dumps(task['data']), headers=self.headers,
                              meta={'task': task}, callback=self.parse_detail)
            else:
                detail_url = task['detail_url'].format(captcha_code=captcha_text)
                yield Request(detail_url, callback=self.parse_detail, meta={'task': task})
        else:
            if self.test_code == 120000:
                task['data']['jym'] = captcha_text
                task['data']['token'] = token
                self.headers['Content-Type'] = 'application/x-www-form-urlencoded'
            elif self.test_code == 360000 or self.test_code == 640000:
                task['data']['yzm'] = captcha_text
                self.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
            elif self.test_code == 370200:
                task['data']['ipt_xm'] = captcha_text
            elif '_csrf' in task['data']:
                task['data']['_csrf'] = response.meta.get('_csrf')
            yield FormRequest(task['detail_url'], formdata=task['data'], headers=self.headers, callback=self.parse_detail, meta={'task': task})

    def parse_detail(self, response):
        self.logger.info(f'Parse Detail: {response.url}')
        print(response.text)
        count = 0
        false = ''
        task = response.meta['task']
        try:
            if task['type'] == 'html':
                if self.test_code == 120000:
                    count = len(response.css('td#textContent fieldset'))
                elif self.test_code == 230000:
                    count = len(response.css('table#dzswj_bb tr')[2:])
                elif self.test_code == 370200:
                    count = len(response.css('.table-scrollable-horizontal tbody.text-dark').extract())
                elif self.test_code == 460000:
                    count = len(response.css('.list_table tr'))
            else:
                text = response.text
                result = json.loads(text)
                if self.test_code == 110000:
                    count = len(eval(result['json'])['data'][0]['resultList'])
                elif self.test_code == 130000:
                    count = len(result.get('value', []))
                elif self.test_code == 350200:
                    count = result.get('total', 0)
                elif self.test_code == 370000:
                    count = result['message'].get('totalRow', 0)
                elif self.test_code == 430000:
                    pass
                elif self.test_code == 440000:
                    count = len(result.get('resultObj', []))
                elif self.test_code == 450000:
                    pprint(result['data'])
                elif self.test_code == 640000:
                    count = len(result['data'][0].get('trs', []))
                pprint(result)
        except Exception as e:
            count = 0
            print(f'Error: {e}')
        finally:
            print(f'count: {count}')