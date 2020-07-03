from scrapy import Spider, FormRequest, Request
import muggle_ocr
import uuid
import json
import random


class EtaxSpider(Spider):
    name = 'test_etax'

    def start_requests(self):
        request_url = 'https://etax.ningxia.chinatax.gov.cn/sword?ctrl=QsggCtrl_initView'
        yield Request(request_url, callback=self.parse_data)


    def parse_data(self, response):
        self.logger.info(f'Parse Data: {response.url}')

        captcha_url = 'https://etax.ningxia.chinatax.gov.cn/download.sword?ctrl=QsggCtrl_getCheckcode'
        yield Request(captcha_url, callback=self.parse_captcha)


    def parse_captcha(self, response):
        self.logger.info(f'Parse Captcha: {response.url}')

        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Host':'etax.ningxia.chinatax.gov.cn',
            'Origin': 'https://etax.ningxia.chinatax.gov.cn',
            'Referer': 'https://etax.ningxia.chinatax.gov.cn/sword?ctrl=QsggCtrl_initView',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
        }

        with open('captcha.jpg', 'wb') as f:
            f.write(response.body)

        captcha_bytes = response.body
        sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
        captcha_text = sdk.predict(image_bytes=captcha_bytes)
        print(f'captcha_text: {captcha_text}')

        test_uuid = ''.join(str(uuid.uuid1()).split('-'))
        request_api = 'https://etax.ningxia.chinatax.gov.cn/ajax.sword?rUUID={}'.format(test_uuid)

        form_data = {
            'nsrsbh': '91640300684214375T',
            'ggrqq': '2017-05-09',
            'ggrqz': '2020-05-09',
            'yzm': captcha_text
        }
    #     # result = eval(data['postData'])
    #     # result['ctrl'] = 'QsggCtrl_queryQsggList?rUUID={}'.format(test_uuid)
    #     # result['data'][3]['value'] = captcha_text
    #     # data['postData'] = str(result)
    #     # print(data)
        yield FormRequest(request_api, formdata=form_data, headers=headers, callback=self.parse_detail)


    def parse_detail(self, response):
        self.logger.info(f'Parse Detail: {response.url}')
        try:
            result = json.loads(response.text)
            print(result)
        except Exception as e:
            print(e)