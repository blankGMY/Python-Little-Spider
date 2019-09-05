import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import bs4
import time


def get_proxy(url):
    try:
        ua=UserAgent(verify_ssl=False)
        header = {'User-Agent': ua.random}#随机请求头
        ua=UserAgent()
        r=requests.get(url,headers=header)
        r.encoding='utf-8'
        html=r.text
    except Exception as e:
        print("获取网页失败",e)

    try:
        soup=BeautifulSoup(html,'html.parser')
        for tr in soup.find('tbody').children:
            if isinstance( tr, bs4.element.Tag ):
                tds=tr.find_all('td')
                ip=tds[0].string#IP地址
                port=tds[1].string#PORT
                type=tds[3].string#类型
                proxy="{{ '{0}':'{1}:{2}'}},".format(type,ip,port)  #非匹配符{}需要写两个
                print(proxy)   #以Python调用代理IP格式打印
    except Exception as x:
        print("获取代理IP失败" ,x)

def main():
    for i in range(1,11):
        url='https://www.kuaidaili.com/free/inha/%s/'%i #爬取1到10页的代理ip
        get_proxy(url)
        time.sleep(1)#休息1秒再爬取下一页，代码运行太快网页没加载出来会报错

if __name__ == '__main__':
    main()
