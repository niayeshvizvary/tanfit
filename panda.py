import pandas as pd
from db_config import *
from sqlalchemy import create_engine

engine=create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:3306/{db_name}?charset=utf8mb4")

df=pd.read_sql("show tables",engine)
print(df)