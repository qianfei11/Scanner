# _*_ coding:utf-8 _*_

from scapy.all import *


def find_firewall(ip, port):
    print("[*] 开始扫描防火墙状态")

    ACK_response = sr1(IP(dst=ip) / TCP(dport=port, flags="A"), timeout=1, verbose=0)
    SYN_response = sr1(IP(dst=ip) / TCP(dport=port, flags="S"), timeout=1, verbose=0)

    if SYN_response == None or ACK_response == None:
        ip_for_firewall = "防火墙状态： " + "open"
        print("firewall (port {}) is open".format(port))
    elif ((ACK_response == None) or (SYN_response == None)) and not (
        (ACK_response == None) and (SYN_response == None)
    ):
        ip_for_firewall = "防火墙状态： " + "open"
        print("firewall (port {}) is open".format(port))
    elif (SYN_response[TCP].flags == 18) and (ACK_response[TCP].flags == 4):
        ip_for_firewall = "防火墙状态： " + "None"
        print("Firewalls (port {}) is close".format(port))
    elif (SYN_response[TCP].flags == 18) and (ACK_response == None):
        ip_for_firewall = "防火墙状态： " + "None"
        print("port {} is filtered".format(port))
    elif (SYN_response == None) and (ACK_response[TCP].flags == 4):
        ip_for_firewall = "防火墙状态： " + "None"
        print("port {} is filtered".format(port))
    else:
        ip_for_firewall = "防火墙状态： " + "None"
        print("port {} is closed or host down".format(port))

    return ip_for_firewall
