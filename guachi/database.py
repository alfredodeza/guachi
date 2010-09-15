import os.path
from sqlite3 import dbapi2 as sqlite

class dbdict(dict):
    
    def __init__(self, path, table='data'):
        dict.__init__(self)
        self.table = 'data'
        self.db_filename = path
        if not os.path.isfile(self.db_filename):
            self.con = sqlite.connect(self.db_filename)
            self.con.execute("create table data (key PRIMARY KEY,value)")
        else:
            self.con = sqlite.connect(self.db_filename)

        self.select_value = "SELECT value FROM %s WHERE key=?" % self.table 
        self.select_key = "SELECT key FROM %s WHERE key=?" % self.table 
        self.update_value = "UPDATE %s SET value=? WHERE key=?" % self.table
        self.insert_key = "INSERT INTO %s (key,value) WHERE key=?" % self.table 
        self.delete_key = "DELETE FROM %s WHERE key=?" % self.table


    def __getitem__(self, key):
        row = self.con.execute("select value from data where key=?",(key,)).fetchone()
        if not row: raise KeyError
        return row[0]
    
    def __setitem__(self, key, item):
        if self.con.execute("select key from data where key=?",(key,)).fetchone():
            self.con.execute("update data set value=? where key=?",(item,key))
        else:
            self.con.execute("insert into data (key,value) values (?,?)",(key, item))
        self.con.commit()
        return dict.__setitem__(self, key, item)
               
    def __delitem__(self, key):
        if self.con.execute("select key from data where key=?",(key,)).fetchone():
            self.con.execute("delete from data where key=?",(key,))
            self.con.commit()
        else:
             raise KeyError
             
    def keys(self):
        return [row[0] for row in self.con.execute("select key from data").fetchall()]

    def _integrity_check(self):
        """Make sure we are doing OK"""
        integrity = self.con.execute("pragma integrity_check").fetchone()
        if integrity == (u'ok',):
            return True
        return False
