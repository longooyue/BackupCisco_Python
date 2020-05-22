# BackupCisco_Python

## 用法

1.1修改telnet.json内的
```json
"HOSTIP": "172.21.37.249",
"Username": "cisco",
"Password": "cisco"
```
1.2修改.\Lib\telnetlib.py 下的
```python
def read_all(self):
    """Read all data until EOF; block until connection closed."""
    self.process_rawq()
    while not self.eof:
        self.fill_rawq()
        self.process_rawq()
    buf = self.cookedq
    self.cookedq = ''
    return buf
```
为

```python
def read_all(self):
    """Read all data until EOF; block until connection closed."""
    self.process_rawq()
    while not self.eof:
        try:
            self.fill_rawq()
            self.process_rawq()
        except:
            break
    buf = self.cookedq
    self.cookedq = ''
    return buf
```

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
第四版是telnet_mutli_WithConfigjson.py 把设备信息换为json 缺点:有一台怎么都连不上去 优点:设备信息完全脱离脚本 
通过修改telnetlib来解决此问题,暂时没遇到其他副作用. 
~~第五版是telnet_mutli_WithConfigjson0.2.py 更换了读取字节的方法 缺点:暂不清 优点:解决上一版的问题~~ 


## 未来修改方向

telnet功能上基本满足最初的需求,接下来的修改是要增加性能(多进程)  
会考虑学习一下ssh的连接方法
