import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Test")
if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler)
    ])

app.listen(8881)
print("Listening to 8881") ######## - For testing purposes
tornado.ioloop.IOLoop.current().start()
