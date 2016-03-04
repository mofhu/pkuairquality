import requests


def Air_alert():
    report = {}
    report["value1"] = "test"
    report["value2"] = "second"
    report["value3"] = "third"
    requests.post(
        "https://maker.ifttt.com/trigger/Air_Test/with/key/{user_key}".format(user_key=""), data=report)

if __name__ == "__main__":
    Air_alert()
