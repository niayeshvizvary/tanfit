import mysql.connector
from db_config import *
def new_database(name):
    conn=mysql.connector.connect(user=db_config['user'],password=db_config['password'],host=db_config['host'])
    cur=conn.cursor()
    cur.execute(f'drop database if exists {name}')
    cur.execute(f'create database if not exists {name}')
    cur.close()
    conn.close()
    print(f'database {name} created')


def create_table_member():
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("""create table member(
          `cid`   bigint unsigned not null AUTO_INCREMENT PRIMARY KEY,
          `name`   varchar(50) not null,
          `address`  text,
          `phone_number`  varchar(11) not null
          );
""")
    cur.close()
    conn.close()
    print(f'table member created')

def  create_table_trainer():
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute(""" create table trainer(
          `id`   int unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `NAME`   VARCHAR(50) NOT NULL,
          `field`   VARCHAR(50)  NOT NULL,
          `address`        text ,
          `PHONE_NUMBER`  VARCHAR(11) NOT NULL
              );
""")
    cur.close()
    conn.close()
    print(f'table trainer created')

def  create_table_class():
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute(""" create table class(
          `id`     int unsigned not null AUTO_INCREMENT PRIMARY KEY,
          `name`     varchar(50) not null,
          `start_time`    varchar(50) not null,
          `end_time`      varchar(50) not null,
          `price`         MEDIUMINT unsigned not null,
          `capacity`      tinyint unsigned,
          `days`          varchar(50) not null default 'everyday',
          `trainer_id`    int unsigned not null,
           FOREIGN KEY (trainer_id) references trainer(id));
""") 
    cur.close()
    conn.close()
    print(f'table class created')


def create_table_registered():
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute(""" create table registered(
          `id`  int unsigned not null AUTO_INCREMENT PRIMARY KEY,
          `date`   datetime not null,
          `member_cid` bigint unsigned not null,
           FOREIGN KEY (member_cid) references member(cid));
""")   
    cur.close()
    conn.close()
    print(f'table registered created')


def  create_table_each_class():
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute("""  create table class_members(
          `total_members`  tinyint unsigned,
          `class_id` int unsigned not null,
          `register_id`  int unsigned not null,
           FOREIGN KEY (class_id) references class(id),
           FOREIGN KEY (register_id) references registered(id),
           PRIMARY KEY (class_id,register_id));
""")      
    cur.close()
    conn.close()
    print(f'table each class created')    

def  create_table_subscription():
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute(""" create table subscription(
          `id`  int unsigned not null AUTO_INCREMENT PRIMARY KEY,
          `name`   varchar(50) not null,
          `start_date`   varchar(50)  not null,
          `end_date`      varchar(50) not null
                );
""")   
    cur.close()
    conn.close()
    print(f'table subscription created')

def  create_table_member_sub():
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute(""" create table register(
          `sub_id`  int unsigned not null ,
          `register_id`  int unsigned not null,
           FOREIGN KEY (sub_id) references subscription(id),
           FOREIGN KEY (register_id) references registered(id),
           PRIMARY KEY (sub_id,register_id));
""")           
    cur.close()
    conn.close()
    print(f'table member_sub created')

if __name__=="__main__":    
    new_database('gym')
    create_table_member()
    create_table_trainer()
    create_table_class()
    create_table_registered()
    create_table_each_class()
    create_table_subscription()
    create_table_member_sub()