import sys

import web

from tiprepo.config import MYSQL_HOST, MYSQL_DB, MYSQL_USER, MYSQL_PASS

web.config.debug = False

print "Creating tables...",
sys.stdout.flush()

db = web.database(dbn='mysql', host=MYSQL_HOST, db=MYSQL_DB,
                  user=MYSQL_USER, pw=MYSQL_PASS)

db.query("""

/*CREATE TABLE repos (
    id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id)
);*/

""")

print "OK."
