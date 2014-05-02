import web

class page:

    def GET(self):
        render = web.template.render('templates/', base='layout')
        return render.index()
