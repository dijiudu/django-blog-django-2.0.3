from __future__ import absolute_import, unicode_literals

# import pymysql
from .celery import app as celery_app
# pymysql.install_as_MySQLdb()

__all__ = ['celery_app']