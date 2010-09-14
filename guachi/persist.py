#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import os.path,UserDict
from sqlite3 import dbapi2 as sqlite

class dbdict(dict):
    ''' dbdict, a dictionnary-like object for large datasets (several Tera-bytes) '''
    
    def __init__(self,dictName):
        dict.__init__(self)
        self.db_filename = "dbdict_%s.sqlite" % dictName
        if not os.path.isfile(self.db_filename):
            self.con = sqlite.connect(self.db_filename)
            self.con.execute("create table data (key PRIMARY KEY,value)")
        else:
            self.con = sqlite.connect(self.db_filename)

    def __getitem__(self, key):
        if not key:
            return "not key!"
        else:
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
