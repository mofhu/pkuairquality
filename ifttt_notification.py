# -*- coding: utf-8 -*-
# PKU air quality
# output to ifttt maker using its API

import requests


def ios_alert(key='dvGhZv2UPNqyJncn8TAXTk', report={}):
    # report = {}
    # report["value1"] = "test"
    # report["value2"] = "second"
    # report["value3"] = "third"
    try:
        requests.post(
            "https://maker.ifttt.com/trigger/pkuairquality/with/key/{user_key}"\
            .format(user_key=key), data=report)
    except requests.exceptions.ConnectionError:
        return 1
    else:
        return 0

if __name__ == "__main__":
    ios_alert()
