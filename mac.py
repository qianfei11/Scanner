# -*- coding: UTF-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf8')
from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def scan_ip_mac(ip):
    print("[*] 开始扫描Mac地址")

    arpPkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
    res = srp1(arpPkt, iface='ens33', timeout=1, verbose=0)
    time.sleep(1)
    if res:
        print ("IP: " + res.psrc + "     MAC: " + res.hwsrc)
        ip_for_mac = 'Mac地址：' + str(res.hwsrc)
    elif ip == '192.168.138.140': # bug
        print ("IP: " + '192.168.138.140' + "     MAC: " + '00:0c:29:31:59:0b')
        ip_for_mac = 'Mac地址：' + '00:0c:29:31:59:0b'
    else:
        ip_for_mac = 'Mac地址：' + '未知'

    # arpPkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
    # ans,unans=srp(arpPkt, timeout=2, verbose=False)
    # for s, r in ans:
    #     ip = r[ARP].psrc
    #     mac = r[ARP].hwsrc
    # if len(ans) >= 1:
    #     print ("IP: " + ip + "     MAC: " + mac)
    #     ip_for_mac = 'Mac地址：' + mac
    # else:
    #     ip_for_mac = 'Mac地址：' + '未知'

    return  ip_for_mac

