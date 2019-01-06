# -*- coding: utf-8 -*-
import os
import re
import requests
from lxml import etree

'''保存结果'''

#
def stringlistsave(save_path, filename, slist):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # 设置保存路径，保存为txt
    path = save_path + "/" + filename + ".txt"
    with open(path, "w+") as fp:
        for s in slist:
        	 # 做了utf8转码,转为终端可识别的码制
            fp.write("%s\t\t%s\n" % (s[0].encode("utf8"), s[1].encode("utf8")))


'''标题筛选'''


def page_info(mypage):
	# 这里的re.findall 返回的是一个元组列表,内容是 (.*?) 中匹配到的内容
	# 析取每个链接的标题和链接
    mypage_info = re.findall(
        r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', mypage,
        re.S)
    return mypage_info


'''页面内容筛选'''


def new_page_info(new_page):
	#将new_page的内容转为html格式的树
    dom = etree.HTML(new_page)
    # 在<tr>下的<td>中的<a>筛选出text
    new_items = dom.xpath('//tr/td/a/text()')
    # 在<tr>下的<td>标签中的<a>标签筛选出链接地址
    new_urls = dom.xpath('//tr/td/a/@href')
    #若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同
    assert (len(new_items) == len(new_urls))
    return zip(new_items, new_urls)


'''捕抓主程，输出日志'''


def spider(url):
    i = 0
    print("抓取中 ", url)
    mypage = requests.get(url).content.decode("gbk")
    # myPage = urllib2.urlopen(url).read().decode("gbk")
    mypageresults = page_info(mypage)
    save_path = u"新闻抓取"
    filename = str(i) + "_" + u"排行榜"
    stringlistsave(save_path, filename, mypageresults)
    i += 1
    for item, url in mypageresults:
        print("抓取中 ", url)
        new_page = requests.get(url).content.decode("gbk")
        # new_page = urllib2.urlopen(url).read().decode("gbk")
        newpageresults = new_page_info(new_page)
        filename = str(i) + "_" + item
        stringlistsave(save_path, filename, newpageresults)
        i += 1


'''启动函数'''
if __name__ == '__main__':
    print("start")
    start_url = "http://news.163.com/rank/"
    spider(start_url)
    print("end")
