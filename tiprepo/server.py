import web

import tiprepo.models.index

urls = (
    '/', 'tiprepo.models.index.Index',
)

app = web.application(urls, globals())

def run():
    app.run()
