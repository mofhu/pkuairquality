# -*- coding: utf-8 -*-
# Author: Mo Frank Hu
# PKU air quality
# main program to run the flow

import time
from pprint import pprint

def main(output_weibo=False, output_ifttt=False):
    # if output_weibo:
    #     import weibo_post
    #     user_password = raw_input("please input user_password: ")
    #     print('user_password inputed. log in to weibo.')
    #     weibo_post.authorize(user_password)
    if output_weibo:
        import weibo_post
    if output_ifttt:
        import ifttt_notification

    while True:
        import get_air_quality
        air_quality = get_air_quality.get_air_quality()
        print(time.strftime(format('%Y-%m-%d, %H:%M:%S'),
                            time.localtime(time.time())))
        print(air_quality)
        if output_weibo:
            import weibo_post
            pprint(weibo_post.post(air_quality))
        if output_ifttt:
            import ifttt_notification
            ifttt_notification.ios_alert(key='dvGhZv2UPNqyJncn8TAXTk',
                report={
                    'value1': air_quality,
                    'value2': '',
                    'value3': '',
                    }
                )
        time.sleep(60*10) # 10min
if __name__ == '__main__':
    main(output_weibo=True, output_ifttt=True)
