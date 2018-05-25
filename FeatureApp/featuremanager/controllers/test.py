import web

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hello, world!'
#Test run
if __name__ == "__main__":
    app.run()
