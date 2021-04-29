# -*- coding: UTF-8 -*-
import web
urls = (
    '/','Index',
    '/upload','Upload',
 )#路由
  
render = web.template.render('template')
  
class Index:
    def GET(self):#函数名时请求方式
        return render.index()
 
class Upload:
    def POST(self):
        info = web.input(file = {})#接收数据
        filename = info['file'].filename
        thisfile = info['file'].file.read()
        with open('static/%s' %filename, 'wb') as f:
            f.write(thisfile)
        s = format('http://127.0.0.1:8000/static/%s' %filename)
        return s

app = web.application(urls, globals())
 
if __name__ == '__main__':#入口函数判断
    app.run()
 
#'Server.py 127.0.0.1:8000'