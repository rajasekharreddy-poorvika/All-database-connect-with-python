"""SQLITE DATABASE"""

import sqlite3
con = sqlite3.connect("pythonsqlite.db")
cur = con.cursor()
cur.execute("""CREATE TABLE emp_1 (fname text,last text,pay integer)""")
con.close()

"""ORACLE DATABASE"""


import cx_Oracle
con = cx_Oracle.connect("username/password@ipaddress/localhost")
cur = con.cursor()
cur.execute("""CREATE TABLE employee(id int,name varchar2(10))""")
con.close()


"""MYSQL DATABASE"""

import MySQLdb
con = MySQLdb.connect("localhost","username","password","database")
cur = con.cursor()
cur.execute("""CREATE TABLE EMPLOYEE (FIRST_NAME  CHAR(20) NOT NULL,LAST_NAME  CHAR(20),AGE INT,SEX CHAR(1),INCOME FLOAT )""")
con.close()

"""MONGO DATABASE"""

from pymongo import MongoClient
client = MongoClient('localhost', 27017)  #by default it take local host and port
db = client.testdb #create a database
