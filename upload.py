# -*- coding: UTF-8 -*-
from Tkinter import *
import tkFileDialog
import requests

# def Upload():
#     print('upload')
#     selectFileName = tkFileDialog.askopenfilename(title='选择文件')#选择文件
     
#     r = requests.post('file:///usr/share/nmap/scripts/', files={'file':open(selectFileName,'rb')})
#     print(r.content.decode('utf-8'))
#     setText = r.content.decode('utf-8')
#     print(setText.__class__)
#     e1.delete(0,END)
#     e1.insert(0,setText)
 
# def Download():
#     link = e1.get()
#     files = requests.get(link)
#     files.raise_for_status()
#     path = tkinter.filedialog.asksaveasfilename()
#     print(files.content)
#     with open(path, 'wb') as f:
#         f.write(files.content)

def upload_file():
    selectFile = tkFileDialog.askopenfilename()  # askopenfilename 1次上传1个；askopenfilenames1次上传多个
    entry1.insert(0, selectFile)
    filename = selectFile.split('/')[-1]
    print(filename)
    # 
    with open(selectFile, 'rb') as f:
        data = f.read()
        print (data)
    with open("/usr/share/nmap/scripts/" + filename, 'wb') as f:
        f.write(data)

root = Tk()

frm = Frame(root)
frm.grid(padx='20', pady='30')
btn = Button(frm, text='上传文件', command=upload_file)
btn.grid(row=0, column=0, ipadx='3', ipady='3', padx='10', pady='20')
entry1 = Entry(frm, width='40')
entry1.grid(row=0, column=1)

root.mainloop()