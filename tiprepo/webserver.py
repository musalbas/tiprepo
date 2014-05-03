import web

from tiprepo.models.index import Index

#web.config.debug = False

urls = (
    '/', 'Index',
)

app = web.application(urls, globals())

def run():
    app.run()
