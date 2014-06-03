# coding: utf-8
import tornado.ioloop
import tornado.web


# 这里只是一个一个类的声明，看看实例化的地方才是重点
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)  # 创建好了监听的socket和开始listen了
    
    # 如果有一个地方raise error了，那么如何处理呢？？？
    # 会什么能够继续执行呢？？？？这个需要好好的处理一下
    tornado.ioloop.IOLoop.instance().start()  # 开始accept和循环吧