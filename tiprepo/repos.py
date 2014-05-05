from tiprepo.config import REPO_SYNC_EXPIRE, REPO_CONTRIBUTORS_SYNC_EXPIRE
from tiprepo.jsonapis import github

def get_repo(db, owner_login, name, sync=True,
             sync_expire=REPO_SYNC_EXPIRE):
    pass

def get_repo_contributors(db, owner_login, name, sync=True,
                          sync_expire=REPO_CONTRIBUTORS_SYNC_EXPIRE):
    pass

def sync_repo(db, owner_login, name):
    data = github('/repos/' + owner_login + '/' + name)

def sync_repo_contributors(db, owner_login, name):
    pass
