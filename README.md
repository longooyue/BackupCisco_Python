# BackupCisco_Python

## 用法

1.修改telnet.json内的
'''
                  "HOSTIP": "172.21.37.249",
                  "Username": "cisco",
                  "Password": "cisco"
'''
2.运行py脚本

待完善
测试过6台交换机，其中一台交换机不管怎么增加time.sleep都会抛出 ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接.
但是telnet客户端是可以连上去

## 修改过程

秉承着同一件事情做两次以上就要简化的信念
开始想要怎么去简化备份配置的过程.考虑到也能增加一点点python经验,就放弃了使用现有工具.

一开始的第一版是在python官网的实例上增加了保存本地文件
第二版是telnet_mutli_BuildinConfig.py 把功能写成函数. 缺点:修改IP不灵活，设备账号密码必须一样
第三版是telnet_mutli_WithConfigfile.py 把设备IP放在脚本外. 缺点:设备账号密码必须一样
第四版是telnet_mutli_WithConfigjson.py 把设备信息换为json 缺点:有一台开启ssh的怎么都连不上去 优点:设备信息完全脱离脚本

## 未来修改方向

telnet功能上基本满足最初的需求,接下来的修改是要增加性能(多线程)
会考虑学习一下ssh的连接方法
