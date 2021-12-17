# Scaner

> 环境：python 3.9</br>
> Python库：matplotlib，python-scapy，threading，python-nmap</br>
> 本机需要安装的程序：nmap</br>
> cript-vulscan配置参考：https://www.jianshu.com/p/3bc47bb361f8</br>
> 
> 1. `finger_os.py`</br>
> >>> 该文件是用来探测操作系统的，其中有一种是基于nmap修改的扫描探测方式。另一种是基于ttl的探测。默认是ttl的。（配置：需要修改nmap_os_db的位置>>> 为本机的相应的位置）</br>
> 2. `scan_port.py`</br>
> >>> 该文件是用来探测开放端口信息的</br>
> 3. `ip_bug.py`</br>
> >>> 该文件是用来探测常见的漏洞的。（需要配置script-vulscan）</br>
> 4. `mac.py`</br>
> >>> 该文件是用来探测mac地址的</br>
> 5. `firewall.py`</br>
> >>> 该文件是用来探测防火墙状态的</br>
> 6. `antivirus_software.py`：</br>
> >>> 该文件是用来探测杀毒软件的</br>
> 7. `scan_ip.py`</br>
> >>> 该文件是用来处理接受的输入同时扫描在线的ip主机并进行排序</br>
> 8. `all_information.py`</br>
> >>> 该文件是将以上的信息进行整合的代码</br>
> 9. `ui.py`</br>
> >>> 该文件是实现UI界面</br>
> 10. `scanner.py`</br>
> >>> 主函数的执行入口</br>
> 
> 该项目在实现上还有很多的不足和缺陷，在后面如果有时间的话还是会继续完善的

Usage:

```python
$ git clone https://github.com/qianfei11/Scanner.git
$ cd Scanner/
$ python3 -m pip install -r requirements.txt
$ ./scanner.py
```
