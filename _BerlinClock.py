# given time input - output berlin clock representation
import datetime


def get_now():
    now = datetime.datetime.now()
    print(now.ctime())
    return now


def get_berlin_single_minute(minute):
    now_min = (minute % 10) // 5
    return now_min


def get_berlin_single_hour(hour):
    now_hour = (hour % 10) % 5
    return now_hour


def get_berlin_five_minute(minute):
    now_five_min = minute // 5
    return now_five_min


def get_berlin_five_hour(hour):
    now_five_hour = hour // 5
    return now_five_hour


def get_berlin_second(second):
    now_sec = ((second % 10) - 1) % 2
    return now_sec


def print_berlin_clock(clock):
    second = 'O'
    five_hour = 'O' * 4
    single_hour = 'O' * 4
    five_min = 'O' * 11
    single_min = 'O' * 4
    berlin = [(second, clock.berlin_second), (five_hour, clock.berlin_five_hour),
              (single_hour, clock.berlin_single_hour), (five_min, clock.berlin_five_minute),
              (single_min, clock.berlin_minute)]
    for b in berlin:
        print(get_toggles(b[0], b[1]))


def get_toggles(time_string, count):
    return time_string.replace('O', 'X', count)


class Clock:
    def __init__(self):
        self.now = get_now()
        self.minute = self.now.minute
        self.second = self.now.second
        self.hour = self.now.hour
        self.berlin_minute = get_berlin_single_minute(self.minute)
        self.berlin_five_minute = get_berlin_five_minute(self.minute)
        self.berlin_single_hour = get_berlin_single_hour(self.hour)
        self.berlin_five_hour = get_berlin_five_hour(self.hour)
        self.berlin_second = get_berlin_second(self.second)
