import asyncio

import tornado.web

class FbiService(object):
    def __init__(self):
        self.cache = {}
    def calc(self,n):
        if n in self.cache:
            return self.cache[n]
        s=1
        for i in range(1,n):
            s*=i
        self.cache[n] = s
        return s
class FbiHandler(tornado.web.RequestHandler):
    service = FbiService()
    def get(self):
        n = int(self.get_argument('n'))
        self.write(str(self.service.calc(n)))


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/fbi",FbiHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())