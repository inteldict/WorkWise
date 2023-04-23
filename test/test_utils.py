import datetime
import unittest

from utils import strfdelta


class TestUtils(unittest.TestCase):
    """
        Some examples:
        '{D:02}d {H:02}h {M:02}m {S:02}s' --> '05d 08h 04m 02s' (default)
        '{W}w {D}d {H}:{M:02}:{S:02}'     --> '4w 5d 8:04:02'
        '{D:2}d {H:2}:{M:02}:{S:02}'      --> ' 5d  8:04:02'
        '{H}h {S}s'                       --> '72h 800s'
    """

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_timedelta(self):
        td = datetime.timedelta(days=5, hours=8, minutes=4, seconds=2)
        formatted_str = strfdelta(td)
        self.assertEqual('05d 08h 04m 02s', formatted_str)

    def test_timedelta_format(self):
        td = datetime.timedelta(weeks=4, days=5, hours=8, minutes=4, seconds=2)
        formatted_str = strfdelta(td, '{W}w {D}d {H}:{M:02}:{S:02}')
        self.assertEqual('4w 5d 8:04:02', formatted_str)

    def test_timedelta_format2(self):
        td = datetime.timedelta(days=5, hours=8, minutes=4, seconds=2)
        formatted_str = strfdelta(td, '{D:2}d {H:2}:{M:02}:{S:02}')
        self.assertEqual(' 5d  8:04:02', formatted_str)

    def test_timedelta_format3(self):
        td = datetime.timedelta(hours=72, seconds=800)
        formatted_str = strfdelta(td, '{H}h {S}s')
        self.assertEqual('72h 800s', formatted_str)


if __name__ == '__main__':
    unittest.main()
