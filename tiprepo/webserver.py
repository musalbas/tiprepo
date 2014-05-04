import web

from tiprepo.models.index import Index
from tiprepo.models.viewrepo import ViewRepo

#web.config.debug = False

urls = (
    '/', 'Index',
    '/(.+)/(.+)', 'ViewRepo',
)

app = web.application(urls, globals())

def run():
    app.run()
