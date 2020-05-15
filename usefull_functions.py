import time


def current_milli_time(t):
    return int(round(t * 1000))


def elapse_time(start_time):
    return time.time() - start_time
