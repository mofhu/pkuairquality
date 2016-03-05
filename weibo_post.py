# -*- coding: utf-8 -*-
# Author: Mo Frank Hu
# PKU air quality
# output to weibo using API

from weibo import APIClient
# https://github.com/michaelliao/sinaweibopy

import requests

def authorize(user_password):
        # http://jas0n.me/2014/12/19/weibo_robot/
    #构造headers信息
    user_agent = (
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.11 (KHTML, like Gecko) '
      'Chrome/20.0.1132.57 Safari/536.11'
    )
    session = requests.session()
    session.headers['User-Agent'] = user_agent
    session.headers['Host'] = 'api.weibo.com'

    #设置全局变量
    APP_KEY = '1512985854' # 请在微博开放平台获取
    APP_SECRET = '88b3af0c0f8b73560653e6c2e22f5120' #请在微博开放平台获取
    CALLBACK_URL = 'http://frank-the-obscure.me/'
    USERID = 'mofrankhu@gmail.com' #微博登陆邮箱
    PASSWORD = user_password #微博登陆密码
    global client, referer_url
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    referer_url = client.get_authorize_url()
    print('referer_url: %s' % referer_url)
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

    code = '72eaf6914196ebdf3dace23dbe764fb6' # manually got code
    #client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
    #                   redirect_uri=CALLBACK_URL)
    r = client.request_access_token(code)
    access_token = r.access_token # 新浪返回的token，类似abc123xyz456
    expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
    # TODO: 在此可保存access token
    client.set_access_token(access_token, expires_in)


def post(post_string):
    print(client.statuses.update.post(status=post_string))
