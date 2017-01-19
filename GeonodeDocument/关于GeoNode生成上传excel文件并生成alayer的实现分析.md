# 概述

## 需求

用户向网站上传excel文件，然后通过网站后台数据处理生成相关layer及其他可视化页面展示。

## 分析：

目前GeoNode支持上传的文件格式为：.shp；.dbf；.shx；.prj;
不支持excel文件。

所以有两种解决方案：

1. 要求用户上传shapefile文件

借助桌面软件ArcGIS将Excel中的点X、Y坐标转换成点Shape格式。

操作说明：

http://jingyan.baidu.com/article/2009576196ed27cb0721b419.html

http://blog.csdn.net/warrenjiang/article/details/48757389


2. 用户上传excel文件，通过后台代码实现

用户上传xls/xlsx文件到Document模块，然后后台转化成Json格式文件写入数据库。通过Geoserver读取数据库字段渲染页面。

[python实现 Excel 转为json](http://blog.csdn.net/jenyzhang/article/details/51898150)

下面是一个简单demo：
```python
# -*- coding:utf-8 -*- 
  
import xlrd  
import json  
import codecs  
import os  
  
#把excel表格中指定sheet转为json  
def Excel2Json(file_path):  
    #打开excel文件  
    if get_data(file_path) is not None:  
        book = get_data(file_path)  
        #抓取所有sheet页的名称  
        worksheets = book.sheet_names()  
        print "该Excel包含的表单列表为：\n"  
        for sheet in worksheets:  
            print ('%s,%s' %(worksheets.index(sheet),sheet))  
        inp = raw_input(u'请输入表单名对应的编号，对应表单将自动转为json:\n')  
        sheet = book.sheet_by_index(int(inp))  
        row_0 = sheet.row(0)     #第一行是表单标题  
        nrows=sheet.nrows       #行号  
        ncols=sheet.ncols       #列号  
  
  
        result={}   #定义json对象  
        result["title"]=file_path   #表单标题  
        result["rows"]=nrows        #行号  
        result["children"]=[]      #每一行作为数组的一项  
        #遍历所有行，将excel转化为json对象  
        for i in range(nrows):  
            if i==0:  
                continue  
            tmp={}  
            #遍历当前行所有列  
            for j in range(ncols):  
                #获取当前列中文标题  
                title_de=str(row_0[j]).decode('unicode_escape')  
                title_cn= title_de.split("'")[1]  
                #获取单元格的值  
                tmp[title_cn]=sheet.row_values(i)[j]  
            result["children"].append(tmp)  
        json_data=json.dumps(result,indent= 4,sort_keys=True).decode('unicode_escape')  
          
        saveFile(os.getcwd(),worksheets[int(inp)],json_data)  
        print json_data  
  
  
# 获取excel数据源  
def get_data(file_path):  
    """获取excel数据源"""  
    try:  
        data = xlrd.open_workbook(file_path)  
        return data  
    except Exception, e:  
        print u'excel表格读取失败：%s' %e  
        return None  
  
def saveFile(file_path,file_name,data):  
    output = codecs.open(file_path+"/"+file_name+".json",'w',"utf-8")  
    output.write(data)  
    output.close()  
  
if __name__ == '__main__':  
    file_path = raw_input(u'请输入excel文件路径：\n')  
    json_data=Excel2Json(file_path)  
```

## 问题

json数据导入存进数据库之后如何使用Geoserver读取并展现。

调用Django中的DataSource模块：(geonode.layers.utils.py 的get_bbox()方法)

`from django.contrib.gis.gdal import DataSource`

需要了解Geoserver怎么从数据库中读取数据以及相应操作的数据表。

## 相关链接

[CSV/Excel upload #145](https://github.com/GeoNode/geonode/issues/145)

[GNIP - Add table join functionality to GeoNode #1915](https://github.com/GeoNode/geonode/issues/1915)