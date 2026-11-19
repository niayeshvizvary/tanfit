import mysql.connector

from db_config import *

def member_data(cid):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("select * from member where cid=%s;",(cid,))
    data=cur.fetchall()
    cur.close()
    conn.close()
    return data

def trainer_data():
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("select * from trainer")
    data=cur.fetchall()
    cur.close()
    conn.close()
    return data


def class_data():
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("select * from class ")
    data=cur.fetchall()
    cur.close()
    conn.close()
    return data

def registerd_data(id):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("select * from registered where id=%s;",(id,))
    data=cur.fetchall()
    cur.close()
    conn.close()
    return data

def each_class_data(id):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("select * from each_class where id=%s;",(id,))
    data=cur.fetchall()
    cur.close()
    conn.close()
    return data


def subscription_data(id):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("select * from subscription where id=%s;",(id,))
    data=cur.fetchall()
    cur.close()
    conn.close()
    return data

def member_subscription_data(id):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("select * from member_subscription where id=%s;",(id,))
    data=cur.fetchall()
    cur.close()
    conn.close()
    return data



if __name__=="__main__": 
    data=member_data(1)
    print(data)

