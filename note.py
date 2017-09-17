"""
websocket
- 本质： magic string
      - 在客户端连接服务端以后 会有一个验证的过程，就是magic string 就是双方需要认识一下
      - 验证，magic string 做的事情
      - 然后第三步才  收发消息

异步非阻塞:
    阻塞式：(django,Flask, Tornado, Bottle)
        一个请求到来 未处理完成，后续一直等待
        解决方案：多线程或进程

    异步非阻塞（存在IO请求）：Tornado
        永远是单进程+单线程


示例 ：非阻塞

class INdexHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        print('start')
        future=Future()
        tornado.ioloop.IOLoop.current().add_timeout(time.time()+10,self.doing)
        yield future
    def doing(self,*args,**kwargs):
        self.write('async')
        self.finesh


示例2：
from tornado.concurrent import Futrue
from tornado import gen

class INdexHandler(RequestHandler):
    @gen.coroutine
    def get(self):




###web 框架
本质就是Futrue 对象，set_result



"""





































