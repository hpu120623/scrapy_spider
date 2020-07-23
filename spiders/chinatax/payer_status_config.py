from urllib.parse import quote

from utils.functools import str_base64


area_dict = {
    110000: {
        'area': '北京', # 1, 不需要验证码
        'request_url': 'http://etax.beijing.chinatax.gov.cn/WSBST/qd/fzchgl/jsp/ggnr.jsp',
        'detail_url': 'http://etax.beijing.chinatax.gov.cn/WSBST//FZCHGL_FYServlet?PBk7QutP=',
        'method': 'post',
        'type': 'json',
        'data': {
            'qxfj': '00',
            'nsrsbh': '110108787751456',
            'nsrmc': quote('高能控股有限公司'),
            'pageNo': '1',
            'pageSize': '10'
        }
    },
    120000: {
        'area': '天津',
        'request_url': 'http://tianjin.chinatax.gov.cn/wzcx/ssxxcx/nsrztCx.jsp',
        'captcha_url': 'http://tianjin.chinatax.gov.cn/wzcx/servlet/code',
        'detail_url': 'http://tianjin.chinatax.gov.cn/wzcx/nsrztCx.action',
        'method': 'post',
        'type': 'html',
        'data': {
            'sfjy': '0',
            'nsrsbh': '120105300725580',
            'nsrmc': '',
            'jym': '',
            'button':  '查     询',
            'struts.token.name': 'token',
            'token': ''
        }
    },
    370000: {
        'area': '山西', # 1, 不需要验证码
        'request_url': 'https://etax.shanxi.chinatax.gov.cn/gzfw/nsrzt',
        'detail_url': 'https://etax.shanxi.chinatax.gov.cn/gzfw/myCommonRemote/commonQuery?sqlid=OnlineSearch_nsrzt',
        'method': 'post',
        'type': 'json',
        'data': {
            'NSR': '140302051973945',
            'captcha': '',
            '_search': 'false',
            'limit': '50',
            'page': '1',
            'sidx': '',
            'sord': 'asc'
        }
    },
    130000: {
        'area': '河北', # 1,
        'request_url': 'https://etax.hebei.chinatax.gov.cn/yhs-web/cxzx/index.html?&id=90062&code=nsrztcx&_lot=1586918042519#/nsrztcx',
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
    210000: {
        'area': '辽宁', # 0, 网站打不开
        'request_url': 'https://etax.liaoning.chinatax.gov.cn/sword?ctrl=LnGdsPortalCtrl_gzcxPageInit&type=gzcx&gzcxurl=https%3A%2F%2Fetax.liaoning.chinatax.gov.cn%2Fsword%3Fctrl%3DLnGdsPortalCtrl_dlqtz%26rk%3Dgzfw&gnlj=/sword?ctrl=NsrztcxCtrl_initView&gnbt=',
        'captcha_url': 'https://etax.liaoning.chinatax.gov.cn/download.sword?ctrl=CheckcodeCtrl_getCheckcode',
        'detail_url': 'https://etax.heilongjiang.chinatax.gov.cn/nologin/xxcx/qscx_jg.jsp',
        'method': 'post',
        'type': 'html',
        'data': {
            'nsrsbh': '21070324266436Z',
            'nsrmc': '',
            'yzm': ''
        }
    },
    310000: {
        'area': '上海', # 1， 验证码识别率低
        'request_url': 'http://shanghai.chinatax.gov.cn/newxbwz/wzfw/yihushi.jsp',
        'captcha_url': 'http://shanghai.chinatax.gov.cn/newxbwz/servlet/GetshowimgSmall',
        'detail_url': 'http://shanghai.chinatax.gov.cn/newxbwz/wzfw/YhscxCtrl-yhsCx.pfv',
        'method': 'post',
        'type': 'html',
        'data': {
            'shhtym': '9131011669293804XG',
            'yzm': ''
        }
    },
    330000: {
        'area': '浙江',
        'request_url': 'https://etax.zhejiang.chinatax.gov.cn/zjgfdacx/sscx/nsrztcx/nsrztcx.html',
        'captcha_url': 'https://etax.zhejiang.chinatax.gov.cn/zjgfdacx/kaptcha.jpg',
        'detail_url': 'https://etax.zhejiang.chinatax.gov.cn/zjgfdacx/nsrztcx/query/330100328120225/{captcha_code}.do',
        'method': 'get',
        'type': 'json'
    },
    360000: {
        'area': '江西',
        'request_url': 'https://etax.jiangxi.chinatax.gov.cn/etax/jsp/portal/sscx/pub_nsrztcx.jsp',
        'captcha_url': 'https://etax.jiangxi.chinatax.gov.cn/etax/jsp/common/loginCode.jsp',
        'detail_url': 'https://etax.jiangxi.chinatax.gov.cn/etax/manage/jsonController?sid=0400160',
        'method': 'post',
        'type': 'json',
        'data': {
            'nsrsbh': '91410322745760055R',
            'yzm': ''
        }
    },
    410000: {
        'area': '河南',
        'request_url': 'http://etax.henan.chinatax.gov.cn/web/dzswj/taxclient/ggfw/query/nsrztcx.html',
        'captcha_url': 'http://etax.henan.chinatax.gov.cn/web/cm/showPictureCode.do',
        'detail_url': 'http://etax.henan.chinatax.gov.cn/web/public/gzfw/ggcx/nsrztcx.do?NSRSBH=91410105742526554R&CUR_USERID=-1&rcode={captcha_code}',
        'method': 'get',
        'type': 'json'
    },
    430000: {
        'area': '湖南', # 0, 反爬，需代理
        'request_url': 'http://hunan.chinatax.gov.cn/taxpayerstatesearch/20190413003982',
        'captcha_url': 'http://hunan.chinatax.gov.cn/kaptcha/getcode',
        'detail_url': 'http://hunan.chinatax.gov.cn/taxpayerstatesearchdo',
        'method': 'post',
        'type': 'json',
        'data': {
            '_csrf': '',
            'sbg': '91430102685031407B',
            'sbh': '91430102685031407B',
            'mc': '',
            'yzm': ''
        }
    },
    440000: {
        'area': '广东', # 1, 验证码识别率低
        'request_url': 'https://www.etax-gd.gov.cn/web-tycx/sscx/gzcx/gsyw/nsrztcx/nsrztcx.jsp?cdId=dlqcd-195&gnDm=gndm-dlqcd-195&gdslxDm=1',
        'captcha_url': 'https://www.etax-gd.gov.cn/web-tycx/gzrk/builderCaptcha.do',
        'detail_url': 'https://www.etax-gd.gov.cn/web-tycx/gzrk/tycxGzrkQuery.do?bw=',
        'method': 'get',
        'type': 'json',
        'bw': {"taxML": {
            "head": {"gid": "311085A116185FEFE053C2000A0A5B63", "sid": "gzcx.qsqycx", "tid": "+", "version": ""},
            "body": {"nsrsbh": "91440600694736126C", "nsrmc": "", "captcha": ""}}}

    },
    460000: {
        'area': '海南',
        'request_url': 'http://hainan.chinatax.gov.cn/bsfw_5_14/',
        'captcha_url': 'http://hainan.chinatax.gov.cn/captcha.svl',
        'detail_url': 'http://hainan.chinatax.gov.cn/bsfw_5_14.json',
        'method': 'post',
        'type': 'html',
        'data': {
            'name': '',
            'payerId': '460040056384939',
            'pageNo': '1',
            'captcha': ''
        }
    },
    500000: {
        'area': '重庆',
        'request_url': 'https://wbjr.chongqing.chinatax.gov.cn/PortalWeb/pages/sscx/cx_nsrzt.html',
        'captcha_url': 'https://wbjr.chongqing.chinatax.gov.cn/captcha.jpg',
        'detail_url': 'https://wbjr.chongqing.chinatax.gov.cn/api/sscx/queryNsrztPages?jsonStr=',
        'method': 'post',
        'type': 'json',
        'bw': {"nsrsbh":"重庆力帆控股有限公司","searchType":"1","identifyCode":""},
        'data': {
            'pageIndex': '0',
            'pageSize': '10',
            'sortField': '',
            'sortOrder': ''
        }
    },
    530000: {
        'area': '云南',
        'request_url': 'http://yunnan.chinatax.gov.cn/ssxxcx/sscx/nsrzt.do',
        'captcha_url': 'http://yunnan.chinatax.gov.cn/ssxxcx/sscx/verifyCode.do',
        'detail_url': 'http://yunnan.chinatax.gov.cn/ssxxcx/sscx/nsrztDetail.do',
        'method': 'post',
        'type': 'json',
        'data': {
            'nsrsbh': '532621399817935',
            'nsrmc': '',
            'randCode': ''
        }
    },
    610000: {
        'area': '陕西', # 0，404, 数据查询出错
        'request_url': 'https://etax.shaanxi.chinatax.gov.cn/tycx-cjpt-web/view/sscx/gzcx/nsrztcx/nsrztcx.jsp',
        'captcha_url': 'https://etax.shaanxi.chinatax.gov.cn/tycx-cjpt-web/cxptGz/builderCaptcha.do',
        'detail_url': '',
        'method': 'get',
        'type': 'json'
    },
    620000: {
        'area': '甘肃',
        'request_url': 'https://etax.gansu.chinatax.gov.cn/wszx-web/apps/views/cx/fzchcx/fzchcx.html',
        'captcha_url': 'https://etax.gansu.chinatax.gov.cn/bszm-web/bszm/captcha.jpg',
        'detail_url': 'https://etax.gansu.chinatax.gov.cn/bszm-web/api/desktop/tax/query/fzch',
        'method': 'get',
        'type': 'json',
        'data': {
            'nsrmc': '靖远县士东商贸有限责任公司',
            'nsrsbh': '91620421MA71BAMG98',
            'pageIndex': '0',
            'pageSize': '10',
            'sortField': '',
            'sortOrder': '',
            'verifyCode': ''
        }
    },
    630000: {
        'area': '青海', # 0, 验证码识别率低
        'request_url': 'https://etax.qinghai.chinatax.gov.cn/tycx-cjpt-web/view/sscx/gzcx/nsrztcx/nsrztcx.jsp?gdslxDm=1&cdId=dlqcd-20&gnDm=sscx.gzcx.nsrztcx',
        'captcha_url': 'https://etax.qinghai.chinatax.gov.cn/tycx-cjpt-web/cxptGz/builderCaptcha.do',
        'detail_url': 'https://etax.qinghai.chinatax.gov.cn/tycx-cjpt-web/cxptGz/tycxGzcxGzrkQuery.do?bw=',
        'method': 'get',
        'type': 'json',
        'bw': {"taxML":{"head":{"gid":"311085A116185FEFE053C2000A0A5B63","sid":"dzswj.gzcx.nsrztcx","tid":" ","version":""},"body":{"sbhmc":"9163010431087511XT","nsrsbh":"9163010431087511XT","nsrmc":"9163010431087511XT","captcha":""}}}
    },
    640000: {
        'area': '宁夏', # 0, 暂未解析通过
        'request_url': 'https://etax.ningxia.chinatax.gov.cn/sword?ctrl=NsrztcxCtrl_initView',
        'captcha_url': 'https://etax.ningxia.chinatax.gov.cn/download.sword?ctrl=CheckcodeCtrl_getCheckcode',
        'detail_url': 'https://etax.ningxia.chinatax.gov.cn/ajax.sword?ctrl=NsrztcxCtrl_doQuery',
        'method': 'get',
        'type': 'json',
        'data': {
            'nsrsbh': '91640522MA75WFNX60',
            'nsrmc': '',
            'yzm': ''
        }
    },
    330200: {
        'area': '宁波',
        'request_url': 'https://etax.ningbo.chinatax.gov.cn/yhs-web/cxzx/index.html?&code=nsrztcx&id=842#/nsrztcx',
        'captcha_url': 'https://etax.ningbo.chinatax.gov.cn/yhs-web/api/yhsyzm/get',
        'detail_url': 'https://etax.ningbo.chinatax.gov.cn/yhs-web/api/nsrzg/query/nsrztcx',
        'method': 'get',
        'type': 'json',
        'data': {
            'nsrmc': '宁波杉杉股份有限公司',
            'shxydm': '91330200704803055M',
            'yzm': ''
        }
    },
    650000: {
        'area': '新疆',
        'request_url': 'https://etax.xinjiang.chinatax.gov.cn/yhs-web/cxzx/index.html#/fzchcx',
        'detail_url': 'https://etax.xinjiang.chinatax.gov.cn/yhs-web/api/fzch/queryFzchxx?sfzjlxDm=103&sfzjhm={company_code}',
        'method': 'get',
        'type': 'json'
    },
    350200: {
        'area': '厦门', # 0, 页面打不开
        'request_url': 'https://etax.xiamen.chinatax.gov.cn:8443/views/nsrgl/nsrzt_query_index.jsp',
        'detail_url': 'https://etax.xiamen.chinatax.gov.cn:8443/bsfw/nsrgl/queryNsrzt.do',
        'method': 'post',
        'type': 'html',
        'data': {
            'NSRSBH': '913502001550106684',
            'NSRMC': '',
            'YZM': '',
            'saveKey': ''
        }
    },
    370200: {
        'area': '青岛',
        'request_url': 'https://etax.qingdao.chinatax.gov.cn:6883/newdzswj/gotoSwdjxxcx.do',
        'captcha_url': 'https://etax.qingdao.chinatax.gov.cn:6883/newdzswj/getVCI',
        'detail_url': 'https://etax.qingdao.chinatax.gov.cn:6883/newdzswj/swdjxxcx.do?validateCode={captcha_code}&nsrsbh={company_code}',
        'method': 'get',
        'type': 'json'
    },
    440300: {
        'area': '深圳', # 0,极验
        'request_url': 'https://etax.shenzhen.chinatax.gov.cn/BsfwtWeb/apps/views/sscx/fzchcx/fzchcx.html',
        # 'captcha_url': 'https://etax.qingdao.chinatax.gov.cn:6883/newdzswj/getVCI',
        'detail_url': 'https://etax.shenzhen.chinatax.gov.cn/api/zzzd/sssxcx/nsrxxcx',
        'method': 'post',
        'type': 'json',
        'data': {
            'pageId': '1',
            'pageLines': '10',
            'nsrmc': '',
            'nsrsbh': '91440300192224550U'
        }
    },
    510000: {
        'area': '四川',
        'request_url': 'https://etax.sichuan.chinatax.gov.cn/yhs-web/cxzx/index.html#/nsrztcx/',
        'captcha_url': 'https://etax.sichuan.chinatax.gov.cn/yhs-web/api/yhsyzm/get',
        'detail_url': 'https://etax.sichuan.chinatax.gov.cn/yhs-web/api/nsrzg/query/nsrztcx',
        'method': 'get',
        'type': 'json',
        'data': {
            'nsrmc': '四川东恒德建材有限公司',
            'shxydm': '91511302MA65QQ4L20',
            'yzm': ''
        }
    },
}