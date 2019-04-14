# 乱序sql执行框架

## Quick-Start
* 1 启动server
> python server.py

* 2 启动不同的client
> python client.py

* 3 启动控制程序
> python start.py

* 4 开始乱序执行sql
> 在start.py的窗口输入: *start*

* 5 结束
> 在start.py的窗口输入: *exit*

## 原理介绍
整体实现是一个基于socket的c/s结构，通过socketserver来与各客户端建立tcp连接，当一个客户端连接成功后会读取本地的sql.txt并将其中的sql指令上传。server建立一个client(ip:port)与sql指令的映射关系：
> {('127.0.0.1', 56782):client1_command1, ('127.0.0.1', 56782):client1_command2, ('127.0.0.1', 56783):client2_command1}

通过单独的控制进程来实现任务下发，乱序执行的遍历结果实质上是全排列的一个变种，同一个客户端的排序是固定的，在*permutation.py*中来实现遍历算法，得到一个客户端执行顺序的一个结果，类似如下的序列结果：
> [('127.0.0.1', 56783), ('127.0.0.1', 56783), ('127.0.0.1', 56782)]

为了实现server对特定client的任务下发，在建立连接之时，我们会保存当前连接的socket。在得到上面的任务执行顺序后，可以通过对client发送对应的指令信息，从而完成整个乱序执行的结果。

## 待改进
* 1 目前的c/s稍显简陋，同时未对大量指令的一个遍历作处理，有可能出现内存放不下的情况。
* 2 sql执行后未做结果验证，这里可以考虑更深入一步的过程监控和结果验证。


## Requirements
* 1 python 2.7
* 2 SocketServer
