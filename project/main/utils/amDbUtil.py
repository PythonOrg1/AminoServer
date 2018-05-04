import pymysql
import sys
from config import confDb
from base import sysout

mTag = "amDbUtil"
mdbHost = confDb.dbHost
mdbport = confDb.dbPort
mdbUser = confDb.dbUser
mdbPwd = confDb.dbPwd
mdbAmino = confDb.dbName

# class dbConnect():
#     def __init__(self):
#         self.


# create database
def connect(dbhost, dbport, dbuser, dbpasswd, dbName):
    try:
        conn = pymysql.connect(host=dbhost, port=int(dbport), user=dbuser, passwd=dbpasswd, db = dbName)
        # cur = conn.cursor()
        # cur.execute('show databases')
        sysout.info(mTag, 'db connect success!')
        return conn
    except Exception as e:
        sysout.err(mTag, 'db connect failed : ' + str(e))


def executeSql(sql):
    conn = connect(mdbHost, mdbport, mdbUser, mdbPwd, mdbAmino)
    cur = conn.cursor()
    res = cur.execute(sql)
    return res


def saveData(sql):
    sysout.info(mTag, sql)
    try:
        conn = connect(mdbHost, mdbport, mdbUser, mdbPwd, mdbAmino)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        sysout.err(mTag, 'db save failed : ' + str(e))
        return False