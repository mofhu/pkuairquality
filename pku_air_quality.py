# -*- coding: utf-8 -*-
# Author: Mo Frank Hu
# PKU air quality
# main program to run the flow

import ast
import time
from pprint import pprint
import io

def get_keys():
    # get keys from key file.
    with io.open('key', 'rb') as f:
        return ast.literal_eval(f.read())

def pretty_time():
    return time.strftime(format('%Y-%m-%d, %H:%M:%S'), 
                         time.localtime(time.time()))

def main(parameters, output_weibo=False, output_ifttt=False):

    if output_weibo:
        import weibo_post
    if output_ifttt:
        import ifttt_notification

    import get_air_quality
    air_quality = get_air_quality.get_air_quality()

    log = open('log.txt', 'wa')

    while True:
        # main loop
        print(pretty_time())
        print(air_quality)
        log.write("{time} {read}\n".format(
            time=pretty_time(),
            read=air_quality))

        if output_weibo:
            return_string = weibo_post.post(air_quality, parameters)
            pprint(return_string)
            log.write("{time} {note}\n".format(
                time=pretty_time(),
                note=return_string))

        if output_ifttt:
            ifttt_notification.ios_alert(key='dvGhZv2UPNqyJncn8TAXTk',
                report={
                    'value1': air_quality,
                    'value2': '',
                    'value3': '',
                    }
                )
            print("{time} ifttt notification".format(time=pretty_time()))
            log.write("{time} ifttt notification \n".format(time=pretty_time()))

        while True:
            # time control loop
            time.sleep(60) # 1min
            print(pretty_time())
            log.write("{time} \n".format(time=pretty_time()))
            air_quality_new = get_air_quality.get_air_quality()
            if air_quality_new != air_quality:
                air_quality = air_quality_new
                break

if __name__ == '__main__':
    parameters = get_keys()
    main(parameters, output_weibo=True, output_ifttt=True)
