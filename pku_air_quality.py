# -*- coding: utf-8 -*-
# Author: Mo Frank Hu
# PKU air quality
# main program to run the flow

import get_air_quality, weibo_post
import time

def main():
    weibo_post.authorize()
    while True:
        air_quality = get_air_quality.get_air_quality()
        print(air_quality)
        weibo_post.post(air_quality)
        time.sleep(60*10) # 10min
if __name__ == '__main__':
    main()