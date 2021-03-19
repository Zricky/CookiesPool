import requests

from cookiespool.db import RedisClient
from cookiespool.config import SINA_ACCOUNT
conn = RedisClient('accounts', 'weibo')


def read():
    sina = open(SINA_ACCOUNT,u'r')
    for account in sina.readlines():
        username, password, extra = account.split('----')
        result = conn.set(username, password)
        print('账号', username, '密码', password)
        print('录入成功' if result else '录入失败')

if __name__ == '__main__':
    read()