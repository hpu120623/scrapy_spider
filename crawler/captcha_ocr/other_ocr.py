import muggle_ocr


class OtherOCR:

    def __init__(self):
        self.sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)

    @staticmethod
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def parse_captcha(self, filename):
        try:
            image = self.get_file_content(filename)
            captcha_text = self.sdk.predict(image_bytes=image)
            if len(captcha_text) >= 4:
                return captcha_text
            else:
                return self.parse_captcha(filename)
        except Exception as e:
            return self.parse_captcha(filename)
