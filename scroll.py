#-*- encoding=utf-8 -*-
from Tkinter import *
 
master = Tk()
master.title("Jason niu工作室")
theLabel=Label(master,text="进入GUI世界，请开始你的表演！\n关于区块链，请问你想学习什么技能？")  
theLabel.pack() 
 
# theLB = Listbox(master,selectmode=EXTENDED) 
# theLB.pack()
 
sb = Scrollbar(master)       
sb.pack(side = RIGHT,fill=Y)
theLB = Listbox(master,yscrollcommand=sb.set) 
theLB.pack(side=LEFT,fill=BOTH)
 
list=["1、应用层","1.1、面向普通用户","1.2、app客户端","1.3、交易网站","2、扩展层","2.1、智能合约","3、协议层之网络层","3.1、共识机制","3.2、P2P网络","3.3、共识机制","3.4、加密技术","4、协议层之存储层"]
for item in list: #for循环添加
    theLB.insert(END,item) 
 
sb.config(command=theLB.yview)
 
theButton = Button(master,text="删除",\
                   command=lambda x=theLB:x.delete(ACTIVE)) 
theButton.pack()
 
mainloop()