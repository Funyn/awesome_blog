#coding:utf-8
import inspect

def get_kw(fn):
    params = inspect.signature(fn).parameters
    print(params)

def a(aaaa,bwww,ccccc='wwww'):
    return True



