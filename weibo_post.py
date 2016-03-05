# -*- coding: utf-8 -*-
# Author: Mo Frank Hu
# PKU air quality
# output to weibo using API

from weibo import APIClient
# https://github.com/michaelliao/sinaweibopy

import requests

def authorize(user_password):
        # http://jas0n.me/2014/12/19/weibo_robot/

    APP_KEY = '1512985854' # 请在微博开放平台获取
    APP_SECRET = '88b3af0c0f8b73560653e6c2e22f5120' #请在微博开放平台获取
    CALLBACK_URL = 'http://frank-the-obscure.me/'
    USERID = 'mofrankhu@gmail.com' #微博登陆邮箱
    PASSWORD = user_password #微博登陆密码

    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    referer_url = client.get_authorize_url()
    # print('referer_url: %s' % referer_url)
    '''
    #获取回调地址的code
    def get_code():
        #构造post数据
        data = {
            'client_id': APP_KEY,
            'redirect_uri': CALLBACK_URL,
            'userId': USERID,
            'passwd': PASSWORD,
            'isLoginSina': '0',
            'action': 'submit',
            'response_type': 'code'
        }

        session.headers['Referer'] = referer_url

        #post数据到服务器
        resp = session.post(
            url = 'https://api.weibo.com/oauth2/authorize',
            data = data
        )

        print('get url: %s' % resp.url)

        #截取回调url中的code
        code = resp.url[-32:]
        print(code)
        return code
    '''
    # 获取URL参数code:
    # https://api.weibo.com/oauth2/authorize?redirect_uri=http%3A//frank-the-obscure.me/&response_type=code&client_id=1512985854

    code = '0b9e70a77bae860c34c02fbffbfd8c00' # manually got code
    #client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
    #                   redirect_uri=CALLBACK_URL)
    r = client.request_access_token(code)
    access_token = r.access_token # 新浪返回的token，类似abc123xyz456
    expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
    print('token:', access_token)
    print('expires in', expires_in)
    client.set_access_token(access_token, expires_in)


def post(post_string):
    APP_KEY = '1512985854' # 请在微博开放平台获取
    APP_SECRET = '88b3af0c0f8b73560653e6c2e22f5120' #请在微博开放平台获取
    CALLBACK_URL = 'http://frank-the-obscure.me/'
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    client.set_access_token(u'2.00Omo86Gej15eB6f8cb3c5abFNuqgC', 1614834322)
    return(client.statuses.update.post(status=post_string))
