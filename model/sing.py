#--*-- coding:utf-8
from functools import wraps

def singleton(cls):
    instance={}
    @wraps(cls)
    def getinstance(*args,**kwargs):
        if cls not in instance:
            instance[cls]=cls(*args,**kwargs)
        return instance[cls]
    return getinstance
@singleton
class MyClass1(object):
    a=1


class My_Singleton():
    def foo(self):
        pass


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Singleton):
    a = 1

my_singleton=My_Singleton()
