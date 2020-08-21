import re
import execjs
import js2py

from selenium import webdriver
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}

def get_521_content():
    req = requests.get('http://www.mafengwo.cn', headers=headers)
    cookies = req.cookies
    cookies = '; '.join(['='.join(item) for item in cookies.items()])
    txt_521 = req.text
    txt_521 = ''.join(re.findall('<script>(.*?)</script>', txt_521))
    return (txt_521, cookies)

def fixed_fun(function):
    print(function)
    func_return = function.replace('eval', 'return')
    resHtml = "function getClearance(){" + func_return + "};"
    ctx = execjs.compile(resHtml)
    temp1 = ctx.call('getClearance')
    s = 'var a' + temp1.split('document.cookie')[1].split("Path=/;'")[0] + "Path=/;';return a;"
    s = re.sub(r'document.create.*?firstChild.href', '"{}"'.format('http://www.mafengwo.cn'), s) 
    #print('s--->',s)
    s=s.replace('return return','return eval')
    resHtml = "function getnewClearance(){" + s + "};"
    ctx = execjs.compile(resHtml)
    jsl_clearance = ctx.call('getnewClearance')
    __jsl_clearance = str(jsl_clearance).split(';')[0]
    #print(jsl_clearance)
    return __jsl_clearance

if __name__ == '__main__':
    driver = webdriver.Firefox()
    #driver.maximize_window()
    url = 'http://www.mafengwo.cn/'
    driver.get(url)
    data = driver.page_source
    
    print(data)
    da = etree.HTML(data)
    print(da)
    t = da.xpath('//div')
    print(t)
    # func = get_521_content()
    # content = func[0]
    # cookie_id = func[1]
    # cookie_id=cookie_id[11:]
    # cookie_id1 = fixed_fun(content)[16:]
    # # print(cookie_id)
    # cookie={
    #     "__jsl_clearance":cookie_id1,
    #     "__jsluid_h":cookie_id
    # }
    # print(cookie)
    # #headers['Cookie'] = cookie_id + ';' + cookie_id1
    #
    # res1 = requests.get('http://www.mafengwo.cn', headers=headers, cookies=cookie)
    # print(res1.text)
    # # element = etree.HTML(res1.text)
    # # print(element)
    # # selectors = element.xpath('//')
    # # for selector in selectors:
    # #     print(selector)
