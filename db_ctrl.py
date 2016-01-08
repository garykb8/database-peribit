from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

from models.game import *

from config import Base, DB_SERVER_URL, DB_SERVER_PORT, DB_ACCOUNT, DB_PASSWORD, DB_NAME

class DBCtrl(object):
    def __init__(self):
        self.engine = create_engine('mysql://' + DB_ACCOUNT + ':' + DB_PASSWORD + '@' + DB_SERVER_URL + ':' + DB_SERVER_PORT + '/' + DB_NAME)

        self.tables = Base.metadata.tables.keys()

    def create_table(self, table_name):
        if table_name in self.tables:
            try:
                Base.metadata.tables[table_name].create(self.engine)
                print 'Create %s' % (table_name)
            except OperationalError as e:
               print e.orig
        elif table_name == 'all':
            Base.metadata.create_all(self.engine)
            print 'Create all'
        else: 
            print 'No table match!'

    def drop_table(self, table_name):
        if table_name in self.tables:
            try:
                Base.metadata.tables[table_name].drop(self.engine)
                print 'Drop %s' % (table_name)
            except OperationalError as e:
               print e.orig
        elif table_name == 'all':
            Base.metadata.drop_all(self.engine)
            print 'Drop all'
        else: 
            print 'No table match!'

    def list_table(self):
        print self.tables

