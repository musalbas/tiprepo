import web

class Index:

    def GET(self):
        render = web.template.render('templates/', base='layout')
        return render.index()
