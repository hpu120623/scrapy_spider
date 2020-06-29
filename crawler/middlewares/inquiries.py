import json

from scrapy.downloadermiddlewares.retry import RetryMiddleware

from crawler.captcha_ocr import BaiDuOCR


class InquiriesCaptchaMiddleware(RetryMiddleware):
    max_times = 5

    def process_response(self, request, response, spider):
        if spider.name == 'chinatax_inquiries':
            task = request.meta['task']
            if request.meta.get('detail', 0):
                if task['area_id'] == 450000:
                    result = json.loads(response.text)
                    if '验证码无效' in result.get('msg'):
                        print(11111111111)
                        return self._retry(request, 'Key Error', spider)
                elif task['area_id'] == 630000:
                    result = json.loads(response.text)
                    if '校验出错' in result.get('message', ''):
                        captcha_text = BaiDuOCR().parse_captcha('captcha.jpg')
                        print(f'captcha_text: {captcha_text}')
                        task['bw']['taxML']['body']['captcha'] = captcha_text
                        detail_url = task['detail_url'] + str(task['bw'])
                        request._set_url(detail_url)
                        return self._retry(request, 'Key Error', spider)
        return response