
#layers 接口说明：

---------------
layerupload
-----------
1.用户需要上传图层时，必须要求用户已经处于登录状态，并且用户有权限执行此操作；

2.当用户在满足1的条件时，通过判断layerupload的请求方式，如果请求方式为get方法，表示用户进入layerupload界面，直接返回或跳转到layerupload模板页面；

3.当用户在满足1的条件时，如果请求方式为post方法表示用户提交上传图层操作；

4.当用户提交upload操作后，在layerupload接口中，首先通过django内置form表单接受到用户上传数据；

5.在geonode中上传文件格式要求是一个文件夹或压缩包，且文件夹或压缩包需包含含有以.dbf、.shp、.shx、.prj结尾的文件：

*.shp:主文件--存储地理要素的几何图形的文件

*.shx:索引文件--存储图形要素与属性信息索引的文件

*.dbf:dBASE表文件--存储要素信息属性的dBase表文件

*.prj:空间参考文件

前三种文件格式内容为必须

关于shape文件详细信息，可见附录：http://blog.csdn.net/cleverysm/article/details/2114006







