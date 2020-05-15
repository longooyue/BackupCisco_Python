# BackupCisco_Python

## 用法

1.修改telnet.json内的

                  "HOSTIP": "172.21.37.249",
                  "Username": "cisco",
                  "Password": "cisco"

2.运行py脚本

待完善
测试过6台交换机，其中一台交换机不管怎么增加time.sleep都会抛出 ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
但是telnet客户端是可以连上去
