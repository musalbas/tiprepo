import web

from tiprepo import repos

class ViewRepo:

    def GET(self, owner_login, name):
        repos.sync_repo(web.ctx.db, owner_login, name)
