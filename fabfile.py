#!/usr/env/bin python3
# -*- coding:utf-8 -*-

import os,sys
from datetime import datetime
from fabric.api import *

#服务器登陆用户名
env.user = 'pyvip'

#服务器管理用户名
env.sudo_user = 'root'

#服务器IP地址
env.host = ['192.168.28.129']

#服务器Mysql密码口令
db_user = 'admin'
db_password = 'Root110qwe'

_TAR_FILE = 'dist-awesome.tar.gz'
#local('..')来运行本地命令

def build():
    includes = ['static','templates','transwarp','favicon.ico','*.py']
    excludes = ['test','*','*.pyc','*.pyo']
    local('rm -f dist/%s'%_TAR_FILE)
    with lcd(os.path.join(os.path.abspath('.'),'www')):
        cmd = ['tar','--dereference','-czvf','../dist/%s'%_TAR_FILE]
        cmd.extend(['--exclude=\'%s\''%ex for ex in excludes])
        cmd.extend(includes)
        local(' '.join(cmd))


_REMOTE_TMP_TAR = '/tmp/%s'%_TAR_FILE
_REMOTE_BASE_DIR = '/srv/awesome'

def deploy():
    newdir = 'www-%s'%datetime.now().strftime('%y-%m-%d_%H.%M.%S')
    #删除已有tar文件：
    run('rm -f %s'%_REMOTE_TMP_TAR)
    #上传新的tar文件
    put('dist/%s'%_TAR_FILE,_REMOTE_TMP_TAR)
    #创建新目录:
    with cd(_REMOTE_BASE_DIR):
        sudo('mkdir %s'%newdir)
    #解压到新目录
    with cd('%s/%s'%(_REMOTE_BASE_DIR,newdir)):
        sudo('tar -xzvf %s'%_REMOTE_TMP_TAR)
    #重置软连接
    with cd(_REMOTE_BASE_DIR):
        sudo('rm -f www')
        sudo('ln -s %s www'%newdir)
        sudo('chown www-data:www-data www')
        sudo('chown -R www-data:www-data %s'%newdir)
    #重启python服务和nginx服务器
    with settings(warn_only=True):
        sudo('supervisorctl stop awesome_blog')
        sudo('supervisorctl start awesome_blog')
        sudo('/etc/init.d/nginx.reload')