import mysql.connector
import datetime

from db_config import *

def insert_member_data(name,address,phone_number):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("insert into member(name,address,phone_number) values(%s,%s,%s);",(name,address,phone_number))
    conn.commit()
    cur.close()
    conn.close()
    print(f'add to member ')

def insert_trainer_data(name,field,address,phone_number):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("insert into trainer(name,field,address,phone_number) values(%s,%s,%s,%s);",(name,field,address,phone_number))
    conn.commit()
    cur.close()
    conn.close()
    print(f'add to trainer ')


def insert_class_data(name,start_time,end_time,price,capacity,days,trainer_id):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("insert into class(name,start_time,end_time,price,capacity,days,trainer_id) values(%s,%s,%s,%s,%s,%s,%s);",(name,start_time,end_time,price,capacity,days,trainer_id))
    conn.commit()
    cur.close()
    conn.close()
    print(f'add to class ')

def insert_registerd_data(date,member_id):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("insert into registered(date,member_id) values(%s,%s);",(date,member_id))
    conn.commit()
    cur.close()
    conn.close()
    print(f'add to registerd ')

def insert_each_class_data(class_id,register_id,total_member=None):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("insert into each_class(class_id,register_id,total_member) values(%s,%s,%s);",(total_member,register_id,class_id))
    conn.commit()
    cur.close()
    conn.close()
    print(f'add to each_class ')


def insert_subscription_data(name,start_date,end_date):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("insert into subscription(name,start_date,end_date) values(%s,%s,%s);",(name,start_date,end_date))
    conn.commit()
    cur.close()
    conn.close()
    print(f'add to subscription ')


def insert_member_subscription_data(sub_id,register_id):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("insert into member_subscription(sub_id,register_id) values(%s,%s);",(sub_id,register_id))
    conn.commit()
    cur.close()
    conn.close()
    print(f'add to subscription ')



if __name__=="__main__": 
    insert_member_data('ali','tehran','09908156793')
    insert_member_data('aram','tehran','09112766680')
    insert_member_data('nia','tehran','09122673591')
    insert_trainer_data('aria','bodybuilding','tehran','09122756347')
    insert_trainer_data('ali','crossfit','tehran','09134556349')
    insert_trainer_data('ava','bodybuilding','tehran','09123473582')
    insert_trainer_data('sara','yoga','tehran','09100773677')
    insert_class_data('pilates','11:00','12:00',30000,20,'evens',3)
    insert_class_data('body bulding','13:00','14:00',30000,20,'odds',1)
    insert_class_data('crossfit','9:00','10:00',30000,20,'evens',2)
    insert_class_data('yoga','8:00','9:00',30000,20,'odds',4)
    insert_class_data('pilates','10:00','11:00',30000,20,'evens',4)

