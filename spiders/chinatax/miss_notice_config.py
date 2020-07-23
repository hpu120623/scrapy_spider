from urllib.parse import quote

from utils.functools import str_base64


area_dict = {
    110000: {
        'area': '北京', # 1
        'request_url': 'http://beijing.chinatax.gov.cn/bjsat/office/jsp/qsgg/query.jsp',
        'detail_url': 'http://so.wedatas.cn/suggest',
        'method': 'post',
        'type': 'json',
        'data': {
                'siteCode': 'bm29010003',
                'qt': '北京清大德人商贸有限公司',
                'tab': 'all',
                'mode': '1',
                'redTitleLength': '24'
        }
    },
    120000: {
        'area': '天津', # 1
        'request_url': 'http://tianjin.chinatax.gov.cn/wzcx/ssggcx.action?cxgglx=8',
        'captcha_url': 'http://tianjin.chinatax.gov.cn/wzcx/servlet/code',
        'detail_url': 'http://tianjin.chinatax.gov.cn/wzcx/xxggCx.action',
        'method': 'post',
        'type': 'html',
        'data': {
            'cxgglx': '8',
            'cxlx': '0',
            'nsrsbh': '120105300725580',
            'nsrmc': '',
            'jym': '',
            'struts.token.name': 'token',
            'token': '' #第一次访问后，源码正则获取
        }
    },
    130000: {
        'area': '河北', # 1
        'request_url': 'https://etax.hebei.chinatax.gov.cn/yhs-web/cxzx/index.html?&id=90029&code=qscx&_lot=1593491319471#/nsrztcx',
        'captcha_url': 'https://etax.hebei.chinatax.gov.cn/yhs-web/api/yhsyzm/get',
        'detail_url': 'https://etax.hebei.chinatax.gov.cn/yhs-web/api/nsrzg/query/nsrztcx',
        'method': 'get',
        'type': 'json',
        'data': {
            'nsrmc': '河北智贞钢铁贸易有限公司',
            'shxydm': '911304045700544144',
            'yzm': ''
        }
    },
    150000: {
        'area': '内蒙', # 0, 网站打不开
        'request_url': 'http://neimenggu.chinatax.gov.cn/nsfw/sscx/',
        'detail_url': 'http://neimenggu.chinatax.gov.cn/nsfw/sscx/qsgg/',
        'method': 'post',
        'type': 'json',
        'data': {
            'QYLX': '企业',
            'GGSQ': '',
            'START': '',
            'END': '',
            'CUR_USERID': '-1'
        }
    },
    230000: {
        'area': '黑龙江', # 1
        'request_url': 'https://etax.heilongjiang.chinatax.gov.cn/nologin/xxcx/qscx.jsp',
        'detail_url': 'https://etax.heilongjiang.chinatax.gov.cn/nologin/xxcx/qscx_jg.jsp',
        'method': 'post',
        'type': 'html',
        'data': {
            'nsrsbh': str_base64('912301106952066966'),
            'fddbr': '',
            'sqq': str_base64('20180610'),
            'sqz': str_base64('20200610')
        }
    },
    350200: {
        'area': '厦门', # 1
        'request_url': 'https://etax.xiamen.chinatax.gov.cn:6011/gzfw/gzcx/qscx/qscxInfo',
        'detail_url': 'https://etax.xiamen.chinatax.gov.cn:6011/gzfw/gzcx/qscx/query',
        'method': 'post',
        'type': 'json',
        'data': {
            'limit': '10',
            'offset': '0',
            'order': 'asc',
            'query.nsrsbh': '913502006852777303',
            'query.nsrmc': '',
            'where': ''
        }
    },
    360000: {
        'area': '江西', # 0，接口返回查询失败
        'request_url': 'https://etax.jiangxi.chinatax.gov.cn/etax/jsp/portal/sscx/pub_szqsggcx.jsp',
        'captcha_url': 'https://etax.jiangxi.chinatax.gov.cn/etax/jsp/common/loginCode.jsp',
        'detail_url': 'https://etax.jiangxi.chinatax.gov.cn/etax/sscxPublicQuery/szqsggcx',
        'method': 'post',
        'type': 'json',
        'data': {
            'nsrsbm': '91360428MA3640MH9G',
            'nsrmc': '',
            'zgswjgmc': '',
            'yzm': ''
        }
    },
    370000: {
        'area': '山西', # 1
        'request_url': 'https://etax.shanxi.chinatax.gov.cn/gzfw/qscx',
        'detail_url': 'https://etax.shanxi.chinatax.gov.cn/gzfw/jkx/extQuery?sqlid=OnlineSearch_QSQK_Nova&LX=1&db=ww',
        'method': 'post',
        'type': 'json',
        'data': {
            '_search': '',
            'limit': '10000',
            'page': '1',
            'sidx': '',
            'sord': 'asc',
            'NSR': '140302051973945',
            'YEAR': '2020',
            'captcha': ''
        }
    },
    370200: {
        'area': '青岛', # 1
        'request_url': 'https://etax.qingdao.chinatax.gov.cn/qsggfzchnewzj_net/qsgg/captchaValidate',
        'captcha_url': 'https://etax.qingdao.chinatax.gov.cn/qsggfzchnewzj_net/qsgg/img',
        'detail_url': 'https://etax.qingdao.chinatax.gov.cn/qsggfzchnewzj_net/qsgg/captchaValidate',
        'method': 'post',
        'type': 'html',
        'data': {
            'ipt_nsrsbh': '91370285MA3MW53Q2U',
            'ipt_nsrmc': '',
            'ipt_fddbrmc': '',
            'ipt_fddbzjh': '',
            'ggrqq': '2018-06-08',
            'ggrqz': '2020-06-08',
            'sel_fj': '13702000000',
            'ipt_xm': ''
        }
    },
    430000: {
        'area': '湖南', # 待验证，ip反爬
        'request_url': 'http://hunan.chinatax.gov.cn/arrears/20190717003534',
        'captcha_url': 'http://hunan.chinatax.gov.cn/kaptcha/getcode',
        'detail_url': 'http://hunan.chinatax.gov.cn/taxpayerstatesearchdo',
        'method': 'post',
        'type': 'json',
        'data': {
            '_csrf': '', # 第一次访问后，源码正则获取
            'sbg': '91430105183846526N',
            'sbh': '91430105183846526N',
            'mc': '',
            'yzm': ''
        }
    },
    440000: {
        'area': '云南', # 1
        'request_url': 'https://etax.yunnan.chinatax.gov.cn/zjgfdacx/sscx/qsggxxcx/qsggxxcx.html',
        'detail_url': 'https://etax.yunnan.chinatax.gov.cn/zjgfdacx/qsggxxcx/query.do?nsrxx=91530103MA6K6BM33W&fddbrxm=&qsrqq=2018-06-07&qsrqz=2020-06-29',
        'method': 'get',
        'type': 'json'
    },
    440300: {
        'area': '深圳', # 0，404
        'request_url': 'https://shenzhen.chinatax.gov.cn/sztax/xxgk/swxzzfgs/shgk/qsxx/common_list.shtml',
        'method': 'post',
        'type': 'json',
        'data': {
            'QYLX': '企业',
            'GGSQ': '',
            'START': '',
            'END': '',
            'CUR_USERID': '-1'
        }
    },
    450000: {
        'area': '广西', # 1，按页码解析入库，建议定向爬取
        'request_url': 'https://etax.guangxi.chinatax.gov.cn:9723/web/dzswj/taxclient/ggfw/qsgg.html',
        'detail_url': 'https://etax.guangxi.chinatax.gov.cn:9723/web/selectDM_ZJ_GG.do',
        'method': 'post',
        'type': 'json',
        'data': {
            'QYLX': '企业',
            'GGSQ': '2020年第1期',
            'START': '1',
            'END': '10',
            'CUR_USERID': '-1'
        }
    },
    640000: {
        'area': '宁夏', # 0, 未解决
        'request_url': 'https://etax.ningxia.chinatax.gov.cn/sword?ctrl=QsggCtrl_initView',
        'captcha_url': 'https://etax.ningxia.chinatax.gov.cn/download.sword?ctrl=QsggCtrl_getCheckcode',
        'detail_url': 'https://etax.ningxia.chinatax.gov.cn/ajax.sword?rUUID=MkcQcrkydWOMTEKwsde4ejzqTPqlR6MY',
        'method': 'post',
        'type': 'json',
        'data': {
            'nsrsbh': '91640300564136456D',
            'ggrqq': '2017-05-09',
            'ggrqz': '2020-06-08',
            'yzm': '',
        }
    },
}