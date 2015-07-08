from os.path import expanduser
from . import util
import os
import sqlite3

class SQLiteRepo:
    _DB_NAME = "oyb.sqlite"
    _DB_PATH = os.path.join(expanduser("~"),".oyb","bmd.sqlite")

    _CREATE_FILES_BKP_INFO_TBL_QUERY = '''CREATE TABLE files_backup_info
        (path text, last_backup_time text, repo_id integer,
    FOREIGN KEY(repo_id) REFERENCES repo(id))'''

    _CREATE_REPO_TBL_QUERY = '''CREATE TABLE repo(id INTEGER PRIMARY KEY,
    name TEXT, created_date TEXT, modified_date TEXT, cred1 TEXT,cred2 TEXT, 
    cred3 TEXT, provider TEXT)'''

    def __init__(self):
        self.db_path  = self._get_db_path()
        if not os.path.isfile(self.db_path):
            self._create_tables()

    def update_status(self, status_list):
        conn = self._get_conn()
        for status in status_list:
            conn.execute('insert into')

    def _get_repo_id(self, backup_source_path):
        query = "select id from repo where path='{0}'".format(backup_source_path)
        conn = self._get_conn()
        

    def _create_tables(self):
        conn = self._get_conn()
        conn.execute(self._CREATE_REPO_TBL_QUERY)
        conn.execute(self._CREATE_FILES_BKP_INFO_TBL_QUERY)
        conn.commit()
        conn.close()

    def _get_conn(self):
        return sqlite3.connect(self.db_path)

    def _get_db_path(self):
        return os.path.join(util.get_user_pref_home(),self._DB_NAME)

if __name__ == '__main__':
    repo = SQLiteRepo()
    //repo.init_repo()
