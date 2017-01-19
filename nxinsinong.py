# -*- coding:utf-8 -*-

import urllib
import urllib2
from lxml import etree

def spider(id,a,y,m,d):
    #头信息，带上cookie，可以模拟登陆
    headers={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;",
            "Cookie":"bdshare_firstime=1484570723386; closeAPP=hide; cn2_forward_url=http%3A%2F%2Fwww.xinsinong.com%2Fprice%2F184%2F; cn2_auth=58806SGCb8RN2YePZF43HhenlaCag2Av3OhvloIN6riO3VjEGUwoLS-P--S-Ab-S-0KMcWbmW9Ma-P-H21m9psR4hMi6mEwCYkxznQ; cn2_username=ajqd0944; CNZZDATA2466903=cnzz_eid%3D2001252194-1484566346-null%26ntime%3D1484566346; Hm_lvt_a9a5d8f377b1522cbcd1c5cca66060f4=1484570716; Hm_lpvt_a9a5d8f377b1522cbcd1c5cca66060f4=1484571566"}
    #spider url
    url="http://www.xinsinong.com/price/id%sa%sy%sm%sd%s.html"%(id,a,y,m,d)
    re = urllib2.Request(url,headers=headers)
    html = urllib2.urlopen(re).read()
    selector = etree.HTML(html)
    vegetables = selector.xpath("//div[@id='results']//tr[@align='center']")
    
    if vegetables:
        j=0
        for i in vegetables:
            if i.xpath("//td[12]/text()"):
                name=i.xpath("//td[1]/text()")[j].encode("utf-8")
                avg=i.xpath("//td[3]/text()")[j].encode("utf-8")
                max=i.xpath("//td[5]/text()")[j].encode("utf-8")
                min=i.xpath("//td[7]/text()")[j].encode("utf-8")
                market=i.xpath("//td[9]/a[1]/text()")[j].encode("utf-8")
                date=i.xpath("//td[12]/text()")[j].encode("utf-8")
                info="name:%s,avg:%s,max:%s,min:%s,market:%s,date:%s"%(name,avg,max,min,market,date)
               
                with open("./vegetables_price.txt","a+") as f:
                    f.write(info)
                    f.write("\n")
                if j < len(vegetables)-1:
                    j += 1
                else:
                    break

def main():
    
     id=int(input("please input product id:"))
     # area=int(input("please input area num:"))
     year=int(input("please input year:"))
     month=int(input("please input month:"))
     day =int(input("please input day:"))
     for area in range(1,32): 
        spider(id,area,year,month,day)
        print("finish area %s"%area)    

if __name__ == "__main__":
    main() 
