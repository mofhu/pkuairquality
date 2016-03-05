import requests


def ios_alert(key='dvGhZv2UPNqyJncn8TAXTk', report={}):
    # report = {}
    # report["value1"] = "test"
    # report["value2"] = "second"
    # report["value3"] = "third"
    requests.post(
        "https://maker.ifttt.com/trigger/pkuairquality/with/key/{user_key}"\
        .format(user_key=key), data=report)

if __name__ == "__main__":
    ios_alert()
