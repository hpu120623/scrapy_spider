import re

from aip import AipOcr


class BaiDuOCR:
    APP_ID = '20428784'
    API_KEY = 'ljHsWF6sxjLLfK1frCKRZm0s'
    SECRET_KEY = 'yyNtlGgqyzBNv14srRofboB8hP09g8wV'

    def __init__(self):
        self.client =  AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    @staticmethod
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()


    def parse_captcha(self, filename):
        image = self.get_file_content(filename)
        result = self.client.basicGeneral(image)
        print(result)
        captcha_text =result['words_result'][0]['words'].strip()
        return captcha_text
