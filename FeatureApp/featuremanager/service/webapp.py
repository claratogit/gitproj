#webapp.py
import web
# etc.

urls = (
    '/', 'index'
)

myglobals = {'countries': [('IE', 'Ireland'), ('UK', 'United Kingdom'), ('US', 'United States')]}

render = web.template.render('templates/', base='testtt', globals=myglobals)
# app = web.application(urls, globals())

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
#rest of app...