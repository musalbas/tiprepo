import sys

import web

from tiprepo.config import MYSQL_HOST, MYSQL_DB, MYSQL_USER, MYSQL_PASS

web.config.debug = False

print "Creating tables...",
sys.stdout.flush()

db = web.database(dbn='mysql', host=MYSQL_HOST, db=MYSQL_DB,
                  user=MYSQL_USER, pw=MYSQL_PASS)

db.query("""

CREATE TABLE repos (

    /* Internal stuff */
    last_synced INT NOT NULL,

    /* Repo-specific */
    gh_id INT NOT NULL,
    PRIMARY KEY (gh_id),
    owner_login VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    forks_count INT NOT NULL,
    stargazers_count INT NOT NULL,
    created_at INT NOT NULL,
    updated_at INT NOT NULL,
    homepage VARCHAR(100),
    organization_login VARCHAR(100),
    organization_avatar_url VARCHAR(100),
    parent_name VARCHAR(100),
    parent_owner_login VARCHAR(100),
    contributors_count INT NOT NULL,

    /* TipRepo-specific */
    total_tipped NUMERIC(20, 8) NOT NULL DEFAULT 0,
    remaining_tipped NUMERIC(20, 8) NOT NULL DEFAULT 0,
    pulls_paid INT NOT NULL DEFAULT 0,
    people_paid INT NOT NULL DEFAULT 0

);

""")

db.query("""

CREATE TABLE repo_contributors (
    id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id),
    repo_gh_id INT NOT NULL,
    contributor_login VARCHAR(100) NOT NULL,
    contributor_gh_id INT NOT NULL,
    commits INT NOT NULL,
    last_synced INT NOT NULL
);

""")

print "OK."
