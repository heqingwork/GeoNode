# 概述
安全模块主要定义资源的安全

GeoNode权限管理主要针对用户和文件两部分构成，具体如下图所示：

![GeoNode权限控制](http://oh6j8wijn.bkt.clouddn.com/QQ20170112-185831.png)

# resource_permissions

描述：资源权限控制

http请求方式：GET/POST

参数说明：

| 参数名称 | 参数说明 | 长度要求 | 是否必须 |
| --- | --- | --- | --- | --- |
| resource_id | 资源id编号 |   | Y |

正常：

如果请求方式为POST：

将请求体转为Python格式，然后调用`set_permissions()`方法

返回状态码：200

如果请求方式为GET：

调用_perms_info_json()方法，`_perms_info_json()`方法用于获取文件所属创作者及群组信息

返回状态码：200

返回内容：json格式

异常：

状态码：401

响应信息：不允许POST与GET之外的请求方式

# set_bulk_permissions

描述：对资源进行权限扩展

http请求方式：POST

正常：

根据资源id获取标题并添加到不允许列表；（此处逻辑没有看懂）

异常：

状态码：400

err_msg：错误的权限说明

# request_permissions

描述：向文件所有者请求下载资源的权限，如果获得uuid，则程序继续执行，否则执行Django的`get_object_or_404()`方法直接跳转到404页面。

http请求方式：POST

正常：调用notification的`send()`方法，向资源所有者发送通知

返回参数：

状态码：200  

异常：返回错误提示

状态码：400

err_msg：通知递送失败

resolve_object（utils）

描述：使用提供的查询解析对象，并核对可选的允许权限

参数说明：

| 参数名称 | 参数说明 | 长度要求 | 是否必须 |
| --- | --- | --- | --- |
| model | 模型对象 |  | Y |
| query | 用于查询模型的字典 |  | N |
| permission | 用于检查的可选权限（默认为`base.view_resourcebase`）|  | N |
| permission_required | 默认为True，为False时允许以GET请求方式继续 |  | N
| permission_msg | 403响应时的可选msg，默认为None |  | N  |

正常：

首先判断资源权限设置是否为真，如果不是，返回404，如果允许为真，判断权限是否在改变图层数据和改变图层样式中，……顺序判断，如果不允许，返回提示。最终返回obj对象。（逻辑还是没看懂）


