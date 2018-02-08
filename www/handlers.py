#!/usr/env/bin python3
# -*- coding:utf-8 -*-

from www.coroweb import get,post
from www.models import User,Blog
import time

@get('/')
async def index(): #缺少参数request
    summary = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    blogs = [
        Blog(id='1',name='Test Blog',summary=summary,created_at=time.time()-120),
        Blog(id='2',name='Second Blog',summary=summary,created_at=time.time()-3600),
        Blog(id='3',name='Burst Blog',summary=summary,created_at=time.time()-7200)
    ]
    return {
        '__template__':'blogs.html',
        'blogs':blogs
    }