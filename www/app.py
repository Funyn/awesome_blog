#!/usr/bin/emv python3
# -*- coding: utf-8 -*-

__author__ = 'FYF'

import logging

logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time
from datetime import datetime
from aiohttp import web
from www.orm import create_pool
from www.models import User



def index(request):
    print(request)
    return web.Response(body='awesome')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000')
    await create_pool(loop,user='root',password='123456',db='fyf')
    user = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await user.save()
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()