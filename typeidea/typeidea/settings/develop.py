#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
module introduction
 
Authors: tanlei(tanlei@baidu.com)
Date:    2019/12/12 10:19 下午
"""
from .base import *     #NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
