# _*_ coding:utf-8 _*_


from nmap import *

#   对于主机存在的漏洞这里我们使用的是nmap进行扫描
'''
具体参数：

nmap -p 80 –script http-iis-short-name-brute +ip(192.168.1.1)[验证iis短文件名泄露] 
nmap -sV -p 11211 -script memcached-info +ip[验证Memcached未授权访问漏洞] 
nmap -sV -（-）script http-vuln-cve2015-1635 +ip[验证http.sys远程代码执行漏洞] 
nmap -sV –script=ssl-heartbleed +ip[验证心脏出血漏洞] 
nmap -p 27017 –script mongodb-info +ip[验证Mongodb未授权访问漏洞] 
nmap -p 6379 –script redis-info +ip[验证Redis未授权访问漏洞] 
nmap –script=http-vuln-cve2015-1427 –script-args command=’ls’ +ip[验证Elasticsearch未授权访问漏洞] 
nmap -p 873 –script rsync-brute –script-args ‘rsync-brute.module=www’ [验证Rsync未授权访问漏洞]
nmap –max-parallelism 800–script http-slowloris scanme.nmap.org  [http 拒绝服务]
nmap -p3306 --script=mysql-empty-password.nse  [mysql空口令登录漏洞]
nmap -p 21 --script ftp-anon.nse -v + ip[检查目标ftp是否允许匿名登录]
'''

def ip_bug_mysql_pwempty(ip):
    print('[*] 开始扫描mysql空口令漏洞')

    # ip_bug_mysql_pwempty
    nm = PortScannerYield()
    bug = nm.scan(ip,arguments='nmap -p3306 --script=mysql-empty-password.nse')

    have_bug = 0

    for i in bug:
        scan = i[1]['scan']
        try:
            if scan:
                info = i[1]['scan'][ip]['tcp'][3306]['script']['mysql-empty-password']
                print(info)
                if info == '\n  root account has empty password\n':
                    ip_bug_mysql = 'mysql空口令漏洞：' + ' 存在'
                    have_bug = 1
                else:
                    ip_bug_mysql = 'mysql空口令漏洞：' + '无'
            else:
                ip_bug_mysql = 'mysql空口令漏洞：' + '无'

        except KeyError:
            ip_bug_mysql = 'mysql空口令漏洞：' + '无'
        print (ip_bug_mysql)
        return  ip_bug_mysql, have_bug
    

def ip_bug_mysql2(ip):
    print('[*] 开始扫描mysql账户密码漏洞')

    # ip_bug_mysql_pwempty
    nm = PortScannerYield()
    bug = nm.scan(ip,arguments='nmap -p3306 --script=mysql-brute.nse')

    have_bug = 0

    for i in bug:
        scan = i[1]['scan']
        try:
            if scan:
                info = i[1]['scan'][ip]['tcp'][3306]['script']['mysql-brute']
                print(info)
                if 'Valid credentials' in info:
                    ip_bug_mysql = 'mysql账户密码漏洞：' + ' 存在'
                    have_bug = 1
                else:
                    ip_bug_mysql = 'mysql账户密码漏洞：' + '无'
            else:
                ip_bug_mysql = 'mysql账户密码漏洞：' + '无'

        except KeyError:
            ip_bug_mysql = 'mysql账户密码漏洞：' + '无'
        print (ip_bug_mysql)
        return  ip_bug_mysql, have_bug

def ip_bug_mysql3(ip):
    print('[*] 开始扫描mysql用户信息')

    # ip_bug_mysql_pwempty
    nm = PortScannerYield()
    bug = nm.scan(ip,arguments='nmap -p3306 --script=mysql-enum.nse')

    have_bug = 0

    for i in bug:
        scan = i[1]['scan']
        try:
            if scan:
                info = i[1]['scan'][ip]['tcp'][3306]['script']['mysql-enum']
                # print(info)
                if 'Valid credentials' in info:
                    info = info.split('\n')[2:-1]
                    info = ''.join([','+a[4:a.index(':')] for a in info])[1:]
                    ip_bug_mysql = 'mysql用户信息：' + info
                    have_bug = 1
                else:
                    ip_bug_mysql = 'mysql用户信息：' + '无'
            else:
                ip_bug_mysql = 'mysql用户信息：' + '无'

        except KeyError:
            ip_bug_mysql = 'mysql用户信息：' + '无'
        print (ip_bug_mysql)
        return  ip_bug_mysql, have_bug

def ip_bug_mysql4(ip):
    print('[*] 开始扫描mysql信息')

    # ip_bug_mysql_pwempty
    nm = PortScannerYield()
    bug = nm.scan(ip,arguments='nmap -p3306 --script=mysql-info.nse')

    have_bug = 0

    for i in bug:
        scan = i[1]['scan']
        try:
            if scan:
                info = i[1]['scan'][ip]['tcp'][3306]['script']['mysql-info']
                # print(info)
                info = info.replace('\n',' ')
                ip_bug_mysql = 'mysql基本信息：' + info
                

                # if 'Valid credentials' in info:
                #     ip_bug_mysql = info
                #     have_bug = 1
                # else:
                #     ip_bug_mysql = 'mysql用户信息：' + '无'
            else:
                ip_bug_mysql = 'mysql信息：' + '无'

        except KeyError:
            ip_bug_mysql = 'mysql信息：' + '无'
        print (ip_bug_mysql)
        return  ip_bug_mysql, have_bug

def ip_bug_mongodb(ip):
    print('[*] 开始扫描Mongodb未授权访问漏洞')

    nm = PortScannerYield()
    bug = nm.scan(ip, arguments='nmap -p27017 --script=mongodb-info.nse')

    have_bug = 0

    for i in bug:
        ip_mongodb = ''
        scan = i[1]['scan']
        try:
            if scan:
                info = i[1]['scan'][ip]['tcp'][27017]['reason']
                print(info)

                if info == 'conn-refused':
                    ip_mongodb = 'Mongodb未授权访问漏洞：' + '无'
                else:
                    ip_mongodb = 'Mongodb未授权访问漏洞：' + '存在'
                    have_bug = 1
            else:
                ip_mongodb = 'Mongodb未授权访问漏洞：' + '无'

        except KeyError:
            ip_mongodb = 'Mongodb未授权访问漏洞：' + '无'

        print (ip_mongodb)
        return ip_mongodb, have_bug


def ip_bug_mongodb2(ip):
    print('[*] 开始扫描Mongodb账户密码漏洞')

    nm = PortScannerYield()
    bug = nm.scan(ip, arguments='nmap -p27017 --script=mongodb-brute.nse')

    have_bug = 0

    for i in bug:
        ip_mongodb = ''
        scan = i[1]['scan']
        try:
            if scan:
                info = i[1]['scan'][ip]['tcp'][27017]['script']['mongodb-brute']
                print(info)

                if 'Accounts: No valid accounts found' in info:
                    ip_mongodb = 'Mongodb账户密码漏洞：' + '无'
                else:
                    ip_mongodb = 'Mongodb账户密码漏洞：' + '存在'
                    have_bug = 1
            else:
                ip_mongodb = 'Mongodb账户密码漏洞：' + '无'

        except KeyError:
            ip_mongodb = 'Mongodb账户密码漏洞：' + '无'

        print (ip_mongodb)
        return ip_mongodb, have_bug

def ip_ftp(ip):
    print('[*] 开始扫描ftp匿名登录漏洞')

    nm = PortScannerYield()
    bug = nm.scan(ip, arguments='nmap -p 21 --script ftp-anon.nse -v')

    have_bug = 0

    # print(bug)
    for i in bug:
        ip_bug_ftp = ''
        try:
            scan = i[1]['scan'][ip]['tcp']
            # print("ftp begin2")

            if scan:
                info = i[1]['scan'][ip]['tcp'][21]['script']['ftp-anon']
                print(info)

                if  info == 'Anonymous FTP login allowed (FTP code 230)':
                    ip_bug_ftp = 'ftp匿名登录漏洞：' + '存在'
                    have_bug = 1
                else:
                    ip_bug_ftp = 'ftp匿名登录漏洞：' + '无'

        except KeyError:

            ip_bug_ftp = 'ftp匿名登录漏洞：' + '无'
        print(ip_bug_ftp)
        return ip_bug_ftp, have_bug

def ip_ftp2(ip):
    print('[*] 开始扫描ftp账户密码漏洞')

    nm = PortScannerYield()
    bug = nm.scan(ip, arguments='nmap -p 21 --script ftp-brute.nse -v')

    have_bug = 0

    # print(bug)
    for i in bug:
        ip_bug_ftp = ''
        try:
            scan = i[1]['scan'][ip]['tcp']
            # print("ftp begin2")

            if scan:
                info = i[1]['scan'][ip]['tcp'][21]['script']['ftp-brute']
                print(info)

                if  'Accounts: No valid accounts found' in info:
                    ip_bug_ftp = 'ftp账户密码漏洞：' + '无'
                    
                else:
                    ip_bug_ftp = 'ftp账户密码漏洞：' + '存在'
                    have_bug = 1

        except KeyError:

            ip_bug_ftp = 'ftp账户密码漏洞：' + '无'
        print(ip_bug_ftp)
        return ip_bug_ftp, have_bug


def ip_ftp3(ip):
    print('[*] 开始扫描ftp服务信息')

    nm = PortScannerYield()
    bug = nm.scan(ip, arguments='nmap -p 21 --script ftp-syst.nse -v')

    have_bug = 0

    # print(bug)
    for i in bug:
        ip_bug_ftp = ''
        try:
            scan = i[1]['scan'][ip]['tcp']
            # print("ftp begin2")

            if scan:
                info = i[1]['scan'][ip]['tcp'][21]['script']['ftp-syst']
                # print(info)

                info = info.replace('\n',' ')
                ip_bug_ftp = 'ftp服务信息：' + info

                # if  'Accounts: No valid accounts found' in info:
                #     ip_bug_ftp = 'ftp账户密码漏洞：' + '无'
                    
                # else:
                #     ip_bug_ftp = 'ftp账户密码漏洞：' + '存在'
                have_bug = 1

        except KeyError:

            ip_bug_ftp = 'ftp服务信息：' + '无'
        print(ip_bug_ftp)
        return ip_bug_ftp, have_bug


def ip_cve(ip):
    print('[*] 开始扫描服务器存在的CVE（vulscan7）')

    nm = PortScannerYield()
    bug = nm.scan(ip, arguments='nmap --script vulscan -sV')

    ip_bug_cve = []

    have_bug = 0

    for i in bug:

        # print (i[1]['scan'][ip]['tcp'].values()[0]['script']['vulscan'])
        try:
            scan = i[1]['scan'][ip]['tcp'].values()[0]['script']['vulscan']
            results = []
            for r in scan.split('\n'):
                have_bug = 1
                if(r.startswith('[')):
                    print (r)
                    ip_bug_cve.append(r)

        except KeyError:
            continue

        return ip_bug_cve, have_bug

def ip_diy(filename, ip):
    print('[*] 开始扫描服务器存在的自定义脚本漏洞')
    print(filename)
    if  filename == []:
        ip_bug_diy = "没有检测到自定义脚本"
        have_bug = 0
    else:
        nm = PortScannerYield()
        bug = nm.scan(ip, arguments='nmap --script {} -sV'.format(filename))
        have_bug = 0

        for i in bug:
            scan = i[1]['scan'][ip]['tcp']
            ip_bug_diy = "自定义漏洞信息：" + str(scan)
            print(ip_bug_diy)

    return  ip_bug_diy,have_bug


