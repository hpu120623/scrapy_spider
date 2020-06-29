from scrapy import Spider, Request


class BaiduSpider(Spider):
    name = 'baidu'

    def start_requests(self):
        yield Request('https://www.baidu.com/')

    def parse(self, response):
        self.logger.info(f'Request End: {response.url}')
        title = response.css('title::text').extract_first()
        print(f'title: {title}')
