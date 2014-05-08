import web

from tiprepo.models.index import Index
from tiprepo.models.viewrepo import ViewRepo
from tiprepo.config import MYSQL_HOST, MYSQL_DB, MYSQL_USER, MYSQL_PASS

#web.config.debug = False

urls = (
    '/', 'Index',
    '/(.+)/(.+)', 'ViewRepo',
)

app = web.application(urls, globals())

db = web.database(dbn='mysql', host=MYSQL_HOST, db=MYSQL_DB,
                  user=MYSQL_USER, pw=MYSQL_PASS)

def hook():
    web.ctx.db = db

app.add_processor(web.loadhook(hook))

def run():
    app.run()
