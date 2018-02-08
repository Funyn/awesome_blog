#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import www.config_default

class Dict(dict):
    """
    自定义字典，但是存在x.y的风格
    """
    def __init__(self,names=(),values=(),**kw):
        super(Dict, self).__init__(**kw)
        for k,v in zip(names,values):
            self[k] = v

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError('Dict object has no attributes %s'%item)

    def __setattr__(self, key, value):
        self[key] = value

def merge(defaults,override):
    r = {}
    for k,v in defaults.items():
        if k in override:
            if isinstance(v,dict):
                r[k] = merge(v,override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r

def toDict(d):
    D = Dict()
    for k,v in d.items():
        D[k] = toDict(v) if isinstance(v,dict) else v
    return D

configs = www.config_default.configs

try:
    import www.config_override
    configs = merge(configs,www.config_override.configs)
except ImportError:
    pass

configs = toDict(configs)