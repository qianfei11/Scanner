# _*_ coding:utf-8 _*_

from antivirus_software import *
from scan_port import *
from mac import *
from firewall import *
from finger_os import *
from ip_bug import *

threads = []
all_ip_all_information = []
all_ip_cve_information = []


class all_infromation:
    def __init__(self, startport, endport, ip_alive_list, vars, filename):
        self.startport = startport
        self.endport = endport
        self.ip_alive_list = ip_alive_list
        self.cve_CheckVar = vars[0]
        self.ftp1_CheckVar = vars[1]
        self.ftp2_CheckVar = vars[2]
        self.ftp3_CheckVar = vars[3]
        self.mysql1_CheckVar = vars[4]
        self.mysql2_CheckVar = vars[5]
        self.mysql3_CheckVar = vars[6]
        self.mysql4_CheckVar = vars[7]
        self.mongodb_CheckVar = vars[8]
        self.mongodb2_CheckVar = vars[9]
        self.diy_CheckVar = vars[10]
        self.have_cve_bug = 0
        self.have_ftp_bug = 0
        self.have_mysql_bug = 0
        self.have_mongodb_bug = 0
        self.filename = filename

    def Threads(self):
        for i in self.ip_alive_list:
            thread = threading.Thread(target=self.all, args=(i,))
            threads.append(thread)
            thread.start()
            thread.join()

    def all(self, ip):
        ip_firewall = ""
        all_port_list = ""
        ip_address = "IP地址为： " + ip
        one_ip_all_infromation = []
        # one_ip_cve_infromation = []
        scaner = ScanPort(self.startport, self.endport, ip)
        ip_for_portlist = scaner.scan_port()

        for port in ip_for_portlist:
            all_port_list = all_port_list + "," + str(port)
        all_port_list = all_port_list[1:]
        ip_port_list = "端口开放情况：" + all_port_list

        if len(ip_for_portlist) == 0:
            ip_firewall == "防火墙状态： open"
        else:
            for port in ip_for_portlist:
                ip_firewall = find_firewall(ip, port)  # 防火墙信息

        ip_mac = scan_ip_mac(ip)  # mac地址信息

        ip_Antivirus_software = find_antivirus_software(ip_for_portlist)  # 杀毒软件类型

        ip_os = find_os(ip)  # 操作系统的类型

        # print(self.mysql_CheckVar)
        # print(self.mongodb_CheckVar)

        if self.mysql1_CheckVar == 1:
            # print('scan mysql port')
            ip_bug_for_mysql, self.have_mysql_bug = ip_bug_mysql_pwempty(ip)  # 主机漏洞扫描
        if self.mysql2_CheckVar == 1:
            # print('scan mysql port')
            ip_bug_for_mysql2, self.have_mysql_bug = ip_bug_mysql2(ip)
        if self.mysql3_CheckVar == 1:
            # print('scan mysql port')
            ip_bug_for_mysql3, self.have_mysql_bug = ip_bug_mysql3(ip)
        if self.mysql4_CheckVar == 1:
            # print('scan mysql port')
            ip_bug_for_mysql4, self.have_mysql_bug = ip_bug_mysql4(ip)
        if self.mongodb_CheckVar == 1:
            # print('scan mongodb port')
            ip_bug_for_mongodb, self.have_mongodb_bug = ip_bug_mongodb(ip)
        if self.mongodb2_CheckVar == 1:
            # print('scan mongodb port')
            ip_bug_for_mongodb2, self.have_mongodb_bug = ip_bug_mongodb2(ip)
        if self.ftp1_CheckVar == 1:
            # print('scan ftp port')
            ip_bug_for_ftp, self.have_ftp_bug = ip_ftp(ip)
        if self.ftp2_CheckVar == 1:
            # print('scan ftp port')
            ip_bug_for_ftp2, self.have_ftp_bug = ip_ftp2(ip)
        if self.ftp3_CheckVar == 1:
            # print('scan ftp port')
            ip_bug_for_ftp3, self.have_ftp_bug = ip_ftp3(ip)
        if self.cve_CheckVar == 1:
            # print('scan cve')
            ip_bug_for_cve, self.have_cve_bug = ip_cve(ip)  # 扫描漏洞结果列表
        if self.diy_CheckVar == 1:
            # print('scan cve')
            ip_bug_for_diy, self.have_diy_bug = ip_diy(self.filename, ip)
        one_ip_all_infromation.append(ip_address)
        one_ip_all_infromation.append(ip_mac)
        one_ip_all_infromation.append(ip_port_list)
        one_ip_all_infromation.append(ip_os)
        one_ip_all_infromation.append(ip_firewall)
        one_ip_all_infromation.append(ip_Antivirus_software)

        if self.mysql1_CheckVar == 1:
            one_ip_all_infromation.append(ip_bug_for_mysql)
        if self.mysql2_CheckVar == 1:
            one_ip_all_infromation.append(ip_bug_for_mysql2)
        if self.mysql3_CheckVar == 1:
            one_ip_all_infromation.append(ip_bug_for_mysql3)
        if self.mysql4_CheckVar == 1:
            one_ip_all_infromation.append(ip_bug_for_mysql4)

        if self.mongodb_CheckVar == 1:
            one_ip_all_infromation.append(ip_bug_for_mongodb)
        if self.mongodb2_CheckVar == 1:
            one_ip_all_infromation.append(ip_bug_for_mongodb2)
        if self.ftp1_CheckVar == 1:
            one_ip_all_infromation.append(ip_bug_for_ftp)
        if self.ftp2_CheckVar == 1:
            one_ip_all_infromation.append(ip_bug_for_ftp2)
        if self.ftp3_CheckVar == 1:
            one_ip_all_infromation.append(ip_bug_for_ftp3)
        # one_ip_all_infromation.append('CVE扫描结果列表')
        # for i in one_ip_all_infromation:
        #     print(i)

        all_ip_all_information.append(one_ip_all_infromation)
        if self.cve_CheckVar == 1:
            all_ip_cve_information.append(ip_bug_for_cve)
        if self.diy_CheckVar == 1:
            one_ip_all_infromation.append(ip_bug_for_diy)

    def get_bug_status(self):
        return [
            self.have_cve_bug,
            self.have_ftp_bug,
            self.have_mysql_bug,
            self.have_mongodb_bug,
        ]


# ip_list = ['10.132.2.158']
#
# a = all_infromation(1,1000,ip_list)
# a.Threads()

# str(member).decode('string_escape')
# for i in all_ip_all_information[0]:
#
#     print(i)
# for i in all_ip_all_information[1]:
#
#     print(i)
