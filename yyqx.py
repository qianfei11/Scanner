#-*- encoding=utf-8 -*-
from nmap import *
from Tkinter import *

nm = PortScannerYield()
bug = nm.scan('192.168.138.141', arguments='nmap --script mysql-enum.nse -p 3306 -v')

for i in bug:
    x = i[1]
    print x

# ListInformation = ['123', '456']

# init_windows = Tk()
# Information = Frame(init_windows)
# ipinformation = LabelFrame(Information, text="局域网主机详细信息")
# ipinformation.pack(padx=10, pady=10)
# listinformation = Listbox(init_windows, height=5,width=70, bd=0)
# for item in ListInformation:
#     listinformation.insert(END, item)
#     if '1' in item:
#         listinformation.itemconfig(END, fg='red')
# listinformation.pack()
# listinformation.delete(0,END)
# # listinformation.pack()
# Information.pack()
# init_windows.mainloop()
