#-*- encoding=utf-8 -*-

import sys, time
 
print("正在下载......")
for i in range(11):
    sys.stdout.write("1\n")
    if i != 10:
        sys.stdout.write("==")
    else:
        sys.stdout.write("== " + str(i*10)+"%/100%")
    sys.stdout.flush()
    time.sleep(0.2)
print("\n" + "下载完成")
