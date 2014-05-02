import web

import codekudos.models.index

urls = (
    '/', 'codekudos.models.index.page',
)

app = web.application(urls, globals())

def run():
    app.run()
