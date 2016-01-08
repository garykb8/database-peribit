import argparse

from db_ctrl import DBCtrl

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--createTable', help='Create tables')
parser.add_argument('-d', '--dropTable', help='Drop tables')
parser.add_argument('-l', '--listTable', help='List available table', action='store_true')
args = parser.parse_args()
db = DBCtrl()

if args.createTable:
    db.create_table(args.createTable)
elif args.dropTable:
    db.drop_table(args.dropTable)
elif args.listTable:
    db.list_table()
else:
    print 'No command match!'

