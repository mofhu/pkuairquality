# -*- coding: utf-8 -*-
# Author: Mo Frank Hu
# PKU air quality
# get air quality module:
# get air quality from 162.105.166.202


def get_air_quality():
    from urllib2 import urlopen, Request, HTTPError

    html = urlopen('http://162.105.166.202').read()

    import re

    # get main data frame from html
    data = re.search(b'MainContent_GridView2.*?本研究数据仅供参考', str(html), re.DOTALL)
    #print(data.group())

    # parse reading of pm2.5
    # sample line: 
    # <td><font face="Times New Roman" color="Black" size="6">PM2.5[30℃]</font></td><td><font face="Times New Roman" color="Black" size="6">308.1</font></td>

    line_PM2_5 = re.search('PM2\.5.*', data.group())

    read_PM2_5 = re.search('(?<=>)[\-0-9\.]+',line_PM2_5.group())

    #print(read_PM2_5.group())
    # parse datetime
    # sample line: 
    # ="6">2016-3-4 16:50:02</font></td>

    datetime = re.search('(?<=="6">)[0-9\- \:]+', data.group())
    #print(datetime.group())
    # output air quality
    air_quality_string = '#PKUairquailty# ' + datetime.group() + ' PM2.5: ' + read_PM2_5.group() + ' ug/m3'
    print(air_quality_string)

    return air_quality_string

if __name__ == '__main__':
     get_air_quality() 