from urllib.parse import quote

from utils.functools import str_base64

area_dict = {
    220000: {
        'area': '吉林', # 1, 常规
        'request_url': 'https://etax.jilin.chinatax.gov.cn:10812/sword?ctrl=LnGdsPortalCtrl_gzcxPageInit&type=gzcx&gzcxurl=https%3A%2F%2Fetax.jilin.chinatax.gov.cn%3A10812%2Fsword%3Fctrl%3DLnGdsPortalCtrl_dlqtz%26rk%3Dgzfw&gnlj=/sword?ctrl=SB708CxqsxxCtrl_initView&gnbt=',
        'captcha_url': 'https://etax.jilin.chinatax.gov.cn:10812/download.sword?ctrl=CheckcodeCtrl_getCheckcode',
        'detail_url': 'https://etax.jilin.chinatax.gov.cn:10812/ajax.sword?ctrl=SB708CxqsxxCtrl_queryQsggList',
        'method': 'post',
        'type': 'json',
        'data': {
            'nsrsbh': '91220000794448105C',
            'ggrqq': '2018-06-17',
            'ggrqz': '2020-06-17',
            'yzm': '',
            'sfjk': '1',
            'vckey': 'sswszmcy_picimg',
            'bindParam': ''
        }
    },
    230000: {
        'area': '黑龙江', # 1，特殊
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
    320000: {
        'area': '江苏', # 1， 常规
        'request_url': 'https://etax.jiangsu.chinatax.gov.cn/jx/commonquery/20181203/3437.html',
        'captcha_url': 'https://etax.jiangsu.chinatax.gov.cn/portal//code.do',
        'detail_url': 'https://etax.jiangsu.chinatax.gov.cn/portal/queryapi/queryGgcxQsxx.do',
        'method': 'post',
        'type': 'json',
        'data': {
            'nsrsbh': '91320506MA1M9B913J',
            'nsrmc': '',
            'yzm': ''
        }
    },
    330000: {
        'area': '浙江',   # 1，常规
        'request_url': 'https://etax.zhejiang.chinatax.gov.cn/zjgfdacx/sscx/qsggxxcx/qsggxxcx.html',
        'captcha_url': 'https://etax.zhejiang.chinatax.gov.cn/zjgfdacx/kaptcha.jpg',
        'detail_url': 'https://etax.zhejiang.chinatax.gov.cn/zjgfdacx/qsggxxcx/query.do?nsrxx=330100328120225&fddbrxm=&qsrqq=2018-06-17&qsrqz=2020-06-17&code={captcha_code}',
        'method': 'get',
        'type': 'json'
    },
    340000: {
        'area': '安徽',   # 1，常规, 接口查不到数据
        'request_url': 'https://etax.anhui.chinatax.gov.cn/qjskggcx?0.3136323235884164',
        'captcha_url': 'https://etax.anhui.chinatax.gov.cn/qsgg/imgCode',
        'detail_url': 'https://etax.anhui.chinatax.gov.cn/qsgg/getggxx',
        'method': 'post',
        'type': 'json',
        'data': {
            'swdjhm': '91341500396840419F',
            'qydwmc': '',
            'ggpc': '',
            'gglx': '1',
            'yzm': '',
            'pageSize': '10',
            'pageNum': '1',
            'cxbz': '0'
        }
    },
    360000: {
        'area': '江西', # 0，常规，接口返回查询失败
        'request_url': 'https://etax.jiangxi.chinatax.gov.cn/etax/jsp/portal/sscx/pub_szqsggcx.jsp',
        'captcha_url': 'https://etax.jiangxi.chinatax.gov.cn/etax/jsp/common/loginCode.jsp',
        'detail_url': 'https://etax.jiangxi.chinatax.gov.cn/etax/sscxPublicQuery/szqsggcx',
        'method': 'post',
        'type': 'json',
        'data': {
            'nsrsbm': '360111158263177',
            'nsrmc': '',
            'zgswjgmc': '',
            'yzm': ''
        }
    },
    370000: {
        'area': '山东',   # 1，返回html
        'request_url': 'https://etax.shandong.chinatax.gov.cn/GgcxQscxAction.do?method=init',
        'captcha_url': 'https://etax.shandong.chinatax.gov.cn/enterprise/login/image.jsp',
        'detail_url': 'https://etax.shandong.chinatax.gov.cn/GgcxQscxAction.do?method=queryData',
        'method': 'post',
        'type': 'html',
        'data': {
            'nsrsbh': '91370000074404905M',
            'nsrmc': '',
            'yzm': ''
        }
    },
    410000: {
        'area': '河南',   # 返回json,日期可选
        'request_url': 'https://etax.henan.chinatax.gov.cn/web/dzswj/taxclient/main_gzfw.html?PARAM=1006',
        'captcha_url': 'https://etax.henan.chinatax.gov.cn/web/cm/showPictureCode.do',
        'detail_url': 'https://etax.henan.chinatax.gov.cn/web/selectDM_ZJ_GG.do?callback=jQuery111107507776522764849_1592381560082',
        'method': 'post',
        'type': 'json',
        'data': {
            'QYLX': '',
            'GGSQ': '2018年欠税公告第三期',
            'YZM': '1',
            'NSRMC': '',
            'NSRSBH': '914101847822007434',
            'rcode': '',
            'START': '1',
            'END': '10',
            'CUR_USERID': '-1',
        }
    },
    420000: {
        'area': '湖北',   # 1, 特殊
        'request_url': 'https://etax.hubei.chinatax.gov.cn/webroot/gzcxAction.do?method=yhsYZM&codename=verifycode_QSGG',
        'captcha_url': 'https://etax.hubei.chinatax.gov.cn/webroot/gzcxAction.do',
        'detail_url': 'https://etax.hubei.chinatax.gov.cn/webroot/gzcxAction.do?method=qsggxxqg',
        'method': 'post',
        'type': 'json',
        'captcha_data': {
            'method': 'checkYZM',
            'yzm': '',
            'verifycode': 'verifycode_QSGG'
        },
        'data': {
            'page': '1',
            'limit': '10',
            'nsrsbh': '91421000063504935H',
            'nsrmc': '',
            'ggrq': '2018-06-17 ~ 2020-06-17',
            'sf': '',
        }
    },
    440000: {
        'area': '广东',   # 1, 特殊
        'request_url': 'https://www.etax-gd.gov.cn/web-tycx/sscx/gzcx/qsqycx/qsqycx.jsp?cdId=cdid-dlqcd-qsqycx&gnDm=gndm-dlqcd-qsqycx&gdslxDm=3',
        'captcha_url': 'https://www.etax-gd.gov.cn/web-tycx/gzrk/builderCaptcha.do',
        'detail_url': 'https://www.etax-gd.gov.cn/web-tycx/gzrk/tycxGzrkQuery.do?t=1592388185670&bw=',
        'method': 'get',
        'type': 'json',
        'bw': {"taxML": {"head": {"gid": "311085A116185FEFE053C2000A0A5B63", "sid": "gzcx.qsqycx", "tid": "+","version": ""},"body": {"nsrsbh": "914412265701910217", "nsrmc": "", "captcha": ""}}}
    },
    450000: {
        'area': '广西',   # 1, 特殊
        'request_url': 'https://etax.guangxi.chinatax.gov.cn:9723/web/dzswj/taxclient/ggfw/query/qscx.html',
        'captcha_url': 'https://etax.guangxi.chinatax.gov.cn:9723/web/cm/showPictureCode.do',
        'detail_url': 'https://etax.guangxi.chinatax.gov.cn:9723/web/selectDM_ZJ_GG.do',
        'method': 'post',
        'type': 'json',
        'data': {
            'QYLX': '企业',
            'GGSQ': '',
            'YZM': '1',
            'NSRMC': '',
            'NSRSBH': '91450103MA5K9L6Q1T',
            'rcode': '',
            'START': '1',
            'END': '10',
            'CUR_USERID': '-1'
        }
    },
    460000: {
        'area': '海南',   # 1, 特殊
        'request_url': 'http://hainan.chinatax.gov.cn/bsfw_5_3/',
        'captcha_url': 'http://hainan.chinatax.gov.cn/captcha.svl',
        'detail_url': 'http://hainan.chinatax.gov.cn/bsfw_5_3.json',
        'method': 'post',
        'type': 'html',
        'data': {
            'name': '',
            'id': '460100056385907',
            'pageNo': '1',
            'captcha': ''
        }
    },
    500000: {
        'area': '重庆',   # 0, 服务器挂
        'request_url': 'https://wbjr.chongqing.chinatax.gov.cn/PortalWeb/pages/sscx/cx_qsqy.html',
        'captcha_url': 'https://wbjr.chongqing.chinatax.gov.cn/captcha.jpg',
        'detail_url': 'https://wbjr.chongqing.chinatax.gov.cn/api/sscx/qsqy',
        'method': 'post',
        'data': {
            "nsrsbh":"915001032038882069",
            "code":""
        }
    },
    520000: {
        'area': '贵州',   # 1, 特殊
        'request_url': 'https://etax.guizhou.chinatax.gov.cn/tycx-cjpt-web/view/sscx/gzcx/qsqycx/qsqycx.jsp',
        'captcha_url': 'https://etax.guizhou.chinatax.gov.cn/tycx-cjpt-web/cxptGz/builderCaptcha.do',
        'detail_url': 'https://etax.guizhou.chinatax.gov.cn/tycx-cjpt-web/cxptGz/tycxGzcxGzrkQuery.do?bw=',
        'method': 'get',
        'type': 'json',
        'bw': {"taxML":{"head":{"gid":"311085A116185FEFE053C2000A0A5B63","sid":"dzswj.gzcx.qsqycx","tid":" ","version":""},"body":{"nsrsbh":"91520115MA6EBTY65P","nsrmc":"","captcha":"","ggrqq":"2020-03-17","ggrqz":"2020-06-17"}}}
    },
    530000: {
        'area': '云南',   # 1, 特殊
        'request_url': 'https://etax.yunnan.chinatax.gov.cn/zjgfdacx/sscx/qsggxxcx/qsggxxcx.html',
        'detail_url': 'https://etax.yunnan.chinatax.gov.cn/zjgfdacx/qsggxxcx/query.do?nsrxx=91530103MA6K628M5T&fddbrxm=&qsrqq=2018-06-17&qsrqz=2020-06-17',
        'method': 'get',
        'type': 'json'
    },
    620000: {
        'area': '甘肃',   # 0, 系统故障接口查询失败
        'request_url': 'https://etax.gansu.chinatax.gov.cn/yhs-web/api/yhsyzm/get',
        'captcha_url': 'https://etax.gansu.chinatax.gov.cn/yhs-web/api/yhsyzm/check', # post
        'detail_url': 'https://etax.gansu.chinatax.gov.cn/yhs-web/api/qsgghxx/xxlbcx',
        'method': 'post',
        'type': 'json',
        'captcha_data': {
            'checknum': ''
        },
        'data': {
            'nd': '2018',
            'nsrsbh': '91620824MA7396D787',
            'pageIndex': '1',
            'pageSize': '10',
            'qsrlx': '00',
            'yzm': ''
        }
    },
    630000: {
        'area': '青海',   # 返回json
        'request_url': 'https://etax.qinghai.chinatax.gov.cn/tycx-cjpt-web/view/sscx/gzcx/qsqycx/qsqycx.jsp?gdslxDm=1&cdId=dlqcd-15&gnDm=dlqcd.gzcx.qsqycx',
        'captcha_url': 'https://etax.qinghai.chinatax.gov.cn/tycx-cjpt-web/cxptGz/builderCaptcha.do',
        'detail_url': 'https://etax.qinghai.chinatax.gov.cn/tycx-cjpt-web/cxptGz/tycxGzcxGzrkQuery.do?gdslxDm=1&bw=',
        'method': 'get',
        'type': 'json',
        'bw': {"taxML":{"head":{"gid":"311085A116185FEFE053C2000A0A5B63","sid":"dzswj.gzcx.qsqycx","tid":"+","version":""},"body":{"nsrsbh":"","nsrmc":"青海合富达基金管理有限公司","captcha":"","ggrqq":"2019-06-17","ggrqz":"2020-06-17"}}}
    },
    650000:{
        'area': '新疆',   # 0，系统故障
        'request_url': 'https://etax.xinjiang.chinatax.gov.cn/yhs-web/api/yhsyzm/get',
        'captcha_url': 'https://etax.xinjiang.chinatax.gov.cn/yhs-web/api/yhsyzm/check', # post,验证码校验
        'detail_url': 'https://etax.xinjiang.chinatax.gov.cn/yhs-web/api/qsgghxx/xxlbcx',
        'method': 'post',
        'type': 'json',
        'captcha_data': {
            'checknum': ''
        },
        'data': {
            'nd': '2019',
            'nsrsbh': '91652801745234303B',
            'pageIndex': '1',
            'pageSize': '10',
            'qsrlx': '00',
            'yzm': ''
        }
    }
}