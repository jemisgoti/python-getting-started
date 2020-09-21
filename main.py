import time


def sayhi():

    print("its worked")
    time.sleep(30)
    sayhi()

sayhi()