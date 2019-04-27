import rethinkdb as r
import json
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
#default config
config_filename = dir_path + "/" + "config.json"

if len(sys.argv) > 1:
    config_filename = sys.argv[1]
config = json.load(open(config_filename,'r'))

rdb_host = config["rdb_host"]
rdb_port = config["rdb_port"]
rdb_dbname = config["rdb_dbname"]
rdb_user = config["rdb_user"]
rdb_pass = config["rdb_pass"]

def insert_elem(item):
    r.db(rdb_dbname).table("tablename").insert(item).run()

def close_connection( con ):
    #print 'rethinkdb exit' , con
    con.close()
    #print 'rethinkdb closed con' , con

def print_cursor(tablename):
    con = r.connect( rdb_host, rdb_port).repl()
    cursor = r.db(rdb_dbname).table(tablename).limit(10000).run(time_format="raw")
    result = []
    for document in cursor:
        line = json.dumps(document)
        print line
        result.append(line)
    #should deal with transactions management
    close_connection(con)

def print_list(tablename):
        con = r.connect( rdb_host, rdb_port).repl()
        cursor = r.db(rdb_dbname).table(tablename).limit(100000).run(time_format="raw")
        result = list(cursor)
        print(json.dumps(result))
        close_connection(con)

print_list("history")
