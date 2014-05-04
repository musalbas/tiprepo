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
    id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id),
    last_synced INT NOT NULL,

    /* Repo-specific */
    owner VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    forks_count INT NOT NULL,
    stargazers_count INT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    homepage VARCHAR(100),
    organization VARCHAR(100),
    organization_avatar_url VARCHAR(100),
    parent VARCHAR(100),
    parent_owner VARCHAR(100),
    contributors_count INT NOT NULL,

    /* TipRepo-specific */
    total_tipped NUMERIC(20, 8) NOT NULL DEFAULT 0,
    remaining_tipped NUMERIC(20, 8) NOT NULL DEFAULT 0,
    pulls_paid INT NOT NULL DEFAULT 0,
    people_paid INT NOT NULL DEFAULT 0

);

""")

print "OK."
