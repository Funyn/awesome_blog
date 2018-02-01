#!/usr/env/bin python3
# -*- coding:utf-8 -*-

import json,logging,inspect,functools

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
