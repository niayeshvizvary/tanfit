from dml import *
from dql import *

def get_class_data():
    class_info=class_data()
    names=[]
    for id in class_info:
        names.append(id[1])


def get_trainer_info():
    trainer_info=trainer_data()
    print(trainer_info)



get_class_data()
get_trainer_info()