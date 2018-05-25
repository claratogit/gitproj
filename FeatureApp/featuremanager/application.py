import web
import config
import featuremanager.controllers

urls = (        

    '/',                                    'featuremanager.controllers.base.index',
    '/clients/',                            'featuremanager.controllers.queries.clients',
    '/productareas/',                       'featuremanager.controllers.queries.productareas',
    '/featurerequests/',                    'app.controllers.module.comment',
    '/module/([0-9]+)/vote/',               'app.controllers.module.vote',
    
    # submit a module
    '/submit/',                             'app.controllers.submit.submit',
)



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()