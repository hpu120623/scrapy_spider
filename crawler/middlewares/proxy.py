import random

from scrapy.downloadermiddlewares.retry import RetryMiddleware


class ProxyMiddleware(RetryMiddleware):

    # 实时代理
    def _set_realtime_proxy(self, request, spider):
        '''
            为了节省代理成本
            1、高概率才使用实时代理
            2、一定概率使用短效代理
                (短效代理一定概率使用本地IP)
        '''
        proxy_demote = request.meta.get('proxy_demote', True)
        if proxy_demote:
            random_int = random.randint(1, 5)
        else:
            random_int = 1

        if random_int == 5:
            self._set_short_proxy(request, spider)
        else:
            request.meta['proxy'] = config.REALTIME_PROXY
            spider.logger.info('Use Proxy: ' + request.meta['proxy'])

    # 设置短效代理
    def _set_short_proxy(self, request, spider):
        '''
            为了节省代理成本
            1、一定概率使用本地IP
        '''
        proxy_demote = request.meta.get('proxy_demote', True)
        if proxy_demote:
            random_int = random.randint(1, 3)
        else:
            random_int = 3

        if random_int != 1:
            request.meta['proxy'] = config.SHORT_PROXY
            spider.logger.info('Use Proxy: ' + request.meta['proxy'])

    # 设置普通代理
    def _set_normal_proxy(self, request, spider):
        proxy = ip_service.get_ip()
        proxy_url = f'{proxy.get("protocol")}://{proxy.get("ip")}:{proxy.get("port")}'
        request.meta['proxy'] = proxy_url
        request.meta['proxy_info'] = proxy
        spider.logger.info('Use Proxy: ' + proxy_url)

    # 设置代理
    def _set_proxy(self, request, spider):
        proxy_type = request.meta.get('proxy_type')

        if not proxy_type:
            return

        if proxy_type == 'realtime':
            self._set_realtime_proxy(request, spider)
        elif proxy_type == 'short':
            self._set_short_proxy(request, spider)
        elif proxy_type == 'normal':
            self._set_normal_proxy(request, spider)

    def process_request(self, request, spider):
        self._set_proxy(request, spider)

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        return self._retry(request, 'Error Proxy', spider)
