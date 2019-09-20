import unittest

from _BerlinClock import Clock, print_berlin_clock


class TestIsBerlinTime(unittest.TestCase):
    def test_is_berlin_time_true(self):
        clock = Clock()
        print_berlin_clock(clock)


if __name__ == '__main__':
    unittest.main()
