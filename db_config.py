import os
from dotenv import load_dotenv
load_dotenv()

db_user=os.environ.get('database_user')
db_password=os.environ.get('database_password')
db_host='localhost'
db_name='gym'


db_config={'user':db_user,'password':db_password,'host':db_host,'database':db_name}