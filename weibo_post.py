# -*- coding: utf-8 -*-
# Author: Mo Frank Hu
# PKU air quality
# output to weibo using API

from weibo import APIClient
# https://github.com/michaelliao/sinaweibopy
import requests

def authorize(user_password, parameters):
    """Get Auth2.0 from weibo.
    """
    # http://jas0n.me/2014/12/19/weibo_robot/

    USERID = 'mofrankhu@gmail.com' #微博登陆邮箱
    PASSWORD = user_password #微博登陆密码

    client = APIClient(app_key=parameters['APP_KEY'], 
                       app_secret=parameters['APP_SECRET'], 
                       redirect_uri=parameters['CALLBACK_URL'])
    referer_url = client.get_authorize_url()
    # print('referer_url: %s' % referer_url)

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


def post(post_string, parameters):
    """Post to weibo.com using string and parameters.

    i: 
        - post string; 
        - parameters (app_key, app_secret, redirect_uri, access_token, expires_in)
    o: post at weibo
    """
    client = APIClient(app_key=parameters['APP_KEY'], app_secret=parameters['APP_SECRET'], redirect_uri=parameters['CALLBACK_URL'])
    client.set_access_token(parameters['ACCESS_TOKEN'], parameters['EXPIRES_IN'])
    return(client.statuses.update.post(status=post_string))
