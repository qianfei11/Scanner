# -*- coding: utf-8 -*-


import platform
import os
import threading
import re

from Tkinter import *

import tkMessageBox as msg



ip_alive_list  = []
#ip_all_information =[['IP地址：   192.168.135.123','Mac地址：   0D:12:W#:21','开放端口:  22,23,43,54,65,76,354,654','操作系统:   /linux','防火墙:   开启','杀毒软件:  360','漏洞:   SQL注入'],['IP地址：   192.168.135.123','Mac地址：   0D:12:W#:21','开放端口:  22,23,43,54,65,76,354,654','操作系统:   /Mac','防火墙:   开启','杀毒软件:  金山','漏洞:   SQL注入']]

class Thread_ip(threading.Thread):     # 多线程扫描
    def __init__(self,threadnum):
        threading.Thread.__init__(self)
        self.threadnum = threadnum

    def run(self):

        find_ip_alive(self.threadnum)


def get_os_information():

    ip_infromation_list = []
    ip_name = platform.node()          #获取主机的名称
    ip_os = platform.architecture()    #主机的操作系统结构
    ip_version = platform.platform()   #获取操作系统名称以及操作系统的版本号 比如'Windows-7-6.1.7601-SP1'
    ip_machine = platform.machine()
    ip_sys = platform.system()         #获取系统
    ip_cpu = platform.processor()
    ip_infromation_list.append(ip_name)
    ip_infromation_list.append(ip_os)
    ip_infromation_list.append(ip_version)
    ip_infromation_list.append(ip_machine)
    ip_infromation_list.append(ip_sys)
    ip_infromation_list.append(ip_cpu)

    return ip_infromation_list

def getip(ipaddr):                 # 获取局域网扫描主机的列表
    ipaddr=ipaddr.replace(' ', '')
    print (ipaddr)
    listip = []
    if  re.match(r'^(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])$',ipaddr) \
        or re.match(r'^(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])-(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])$',ipaddr) \
        or re.match(r'^(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])(,(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5]))+$',ipaddr):

        if '-' in ipaddr:
            ipaddr_split = ipaddr.split("-")
            startip = ipaddr_split[0]
            endip = ipaddr_split[1]
            startip_split = startip.split(".")
            endip_split = endip.split(".")
            start_ip_split = int(startip_split[3])
            end_ip_split = int(endip_split[3])+1 
            ipaddr_3 = startip_split[0] + '.' +startip_split[1] + '.' + startip_split[2] + '.'

            for i in range(start_ip_split,end_ip_split):
                listip.append(ipaddr_3 + str(i))
        elif ',' in ipaddr:
            ipaddr_split = ipaddr.split(",")
            for ip in ipaddr_split:
                listip.append(ip)
        else:
            listip.append(ipaddr)
    else:
        msg.showerror('输入错误','请输入正确的IP地址！！！')
        raise Exception('请输入正确IP')


    print listip
    return listip

def getport(port):                    # 获取扫描的起始端口和结束端口

    if  re.match('^\d{1,5}-\d{1,5}$',port) \
        or re.match('^\d{1,5}$',port):
        if '-' in port:
            port_split = port.split("-")
            startport = port_split[0]
            endport = port_split[1]
        else:
            startport = port
            endport = port
    else:
        msg.showerror('输入错误','请输入正确端口地址！！！')
        raise Exception('请输入正确端口地址')

    print (startport,endport)

    return startport,endport

def find_ip_alive(ip): # ICMP协议可能被屏蔽

    # packet = IP(dst=host, ttl=64, id=ip_id) / ICMP(id=icmp_id, seq=icmp_seq)
    # ping = sr1(packet, timeout=2, verbose=False)
    # if ping:
    #     return 0
    # else:
    #     return -1
    # ip_alive_list = []

    cmd = ['ping', '-c 6', ip]

    output = os.popen(" ".join(cmd)).readlines()
    # print(output)

    flag = False
    for line in list(output):
        if not line:
            continue
        if (str(line).upper().find("timeout") >=0) and (str(line).upper().find("TTL") >= 0):
            continue
        if (str(line).upper().find("TTL") < 0) and (str(line).upper().find("timeout") >=0):
            continue
        if (str(line).upper().find("TTL") >= 0) and (str(line).upper().find("timeout") <0):
            flag = True
            break
    # print(flag)
    if flag:
        ip_alive_list.append(ip)
        print("[*]  ip: %s is online " % (ip))
    # else:
    #     msg.showerror('输入错误','该主机不在线！！！')
    #     raise Exception('没有扫描到存在的IP地址')
    # print("结束")

def threads_find_ip(listip):       # 查看局域网中存活的主机

    for i in listip:

        # thread_ping = threading.Thread(target=find_ip_alive,args=(i,))
        # threads.append(thread_ping)
        # thread_ping.start()
    #thread_ping.join()

        ping_thread = Thread_ip(i)
        ping_thread.start()
    ping_thread.join()
    # print (ip_alive_list)

def scan_os_ip():
    pass

def sort_alive_ip(ip_alive_list):         # 对ip地址进行排序

    ip_alive_list.sort(lambda x, y: cmp(''.join([i.rjust(3, '0') for i in x.split('.')]),
                                        ''.join([i.rjust(3, '0') for i in y.split('.')])))



# ip = getip('10.132.2.1-10.132.2.150')
# threads_find_ip(ip)
# sort_alive_ip(ip_alive_list)
# print (ip_alive_list)
