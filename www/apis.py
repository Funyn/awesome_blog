#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json,logging,inspect,functools

class Page:
    """
    显示页数
    """
    def __init__(self,item_count,page_index=1,page_size=10):
        self.item_count = item_count
        self.page_size = page_size
        self.page_count = item_count // page_size + (1 if item_count % page_size > 0 else 0 )
        if (item_count == 0) or (page_index > self.page_count):
            self.offset = 0
            self.limit = 0
            self.page_index = 1
        else:
            self.page_index = page_index
            self.offset = self.page_size * (page_index-1)
            self.limit = self.page_size
        self.has_next = self.page_index < self.page_count
        self.has_previous = self.page_index > 1

    def __str__(self):
        return 'item_count:%s ,page_count:%s,page_index:%s,page_size:%s,offset:%s,limit:%s'%(
            self.item_count,
            self.page_count,
            self.page_index,
            self.page_size,
            self.offset,
            self.limit)

    __repr__ = __str__

class APIError(Exception):
    """
    基本的API错误信息
    """
    def __init__(self,error,data='',message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

class APIValueError(APIError):
    """
    非法输入的错误信息
    """
    def __init__(self,field,message=''):
        super(APIValueError, self).__init__('value:invalid',field,message)

class APIResourceNotFound(APIError):
    """
    资源找不到的错误信息
    """
    def __init__(self,field,message=''):
        super(APIResourceNotFound, self).__init__("value:not found",field,message)

class APIPermissionError(APIError):
    """
    API没有响应权限
    """
    def __init__(self,message=''):
        super().__init__('permission:forbidden','permission',message)
