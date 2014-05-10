import re
import time
import urllib2

from tiprepo.config import REPO_SYNC_EXPIRE, REPO_CONTRIBUTORS_SYNC_EXPIRE
from tiprepo.jsonapis import github, github_unixtime

class InvalidRepoError(Exception):
    pass

def get_repo(db, owner_login, name, sync=True,
             sync_expire=REPO_SYNC_EXPIRE):
    db_vars = dict(owner_login = owner_login, name = name)
    results = db.select('repos', vars=db_vars,
                       where='owner_login = $owner_login AND name = $name')

    if len(results) > 0:
        repo = results[0]
        if (not sync
            or not time.time() - repo.last_synced > sync_expire):
            return repo
    elif not sync:
        raise InvalidRepoError("The repo '" + owner_login + "/" + name
                               + "' has not been synced.")

    return sync_repo(db, owner_login, name)

def get_repo_contributors(db, owner_login, name, sync=True,
                          sync_expire=REPO_CONTRIBUTORS_SYNC_EXPIRE):
    pass

def sync_repo(db, owner_login, name):
    try:
        api_data = github('/repos/' + owner_login + '/' + name)
        # We have to get the contributors count from the HTML page as the
        # GitHub API doesn't provide it.
        html_data = urllib2.urlopen('https://github.com/' + owner_login
                                    + '/' + name
                                    + '/contributors_size').read()
    except urllib2.HTTPError as e:
        raise InvalidRepoError(str(e))

    contributors_count = re.findall(r'<span class="octicon octicon-organization"></span>\s*[0-9,]+\s*</span>',
                                    html_data)
    contributors_count = re.sub(r'<.*?>', '', contributors_count[0])
    contributors_count = contributors_count.replace(',', '')
    contributors_count = int(contributors_count.strip())

    last_synced = time.time()
    gh_id = api_data['id']
    owner_login = api_data['owner']['login']
    name = api_data['name']
    forks_count = api_data['forks_count']
    stargazers_count = api_data['stargazers_count']
    homepage = api_data['homepage']

    created_at = github_unixtime(api_data['created_at'])
    updated_at = github_unixtime(api_data['updated_at'])

    if 'organization' in api_data:
        organization_login = api_data['organization']['login']
        organization_avatar_url = api_data['organization']['avatar_url']
    else:
        organization_login = organization_avatar_url = None

    if 'parent' in api_data:
        parent_name = api_data['parent']['name']
        parent_owner_login = api_data['parent']['owner']['login']
    else:
        parent_name = parent_owner_login = None

    db_vars = dict(gh_id = gh_id)
    updated = db.update('repos', vars=db_vars, where='gh_id = $gh_id',
                        owner_login=owner_login,
                        name=name,
                        forks_count=forks_count,
                        stargazers_count=stargazers_count,
                        created_at=created_at,
                        updated_at=updated_at,
                        homepage=homepage,
                        organization_login=organization_login,
                        organization_avatar_url=organization_avatar_url,
                        parent_name=parent_name,
                        parent_owner_login=parent_owner_login,
                        contributors_count=contributors_count,
                        last_synced=last_synced
                        )

    # TODO use db.select to check if the repo already exists in the db
    # before inserting it, in case db.update returns 0 if nothing gets
    # updated (which should only happens if this function is called twice
    # in the same second).
    if updated == 0:
        db.insert('repos',
                  gh_id=gh_id,
                  owner_login=owner_login,
                  name=name,
                  forks_count=forks_count,
                  stargazers_count=stargazers_count,
                  created_at=created_at,
                  updated_at=updated_at,
                  homepage=homepage,
                  organization_login=organization_login,
                  organization_avatar_url=organization_avatar_url,
                  parent_name=parent_name,
                  parent_owner_login=parent_owner_login,
                  contributors_count=contributors_count,
                  last_synced=last_synced
                  )

    return get_repo(db, owner_login, name, sync=False)

def sync_repo_contributors(db, owner_login, name):
    pass
