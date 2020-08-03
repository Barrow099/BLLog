import unittest
import datetime

import bllog
from bllog import LogFormatter
from bllog.log_classes import LogLevel
from bllog.logger import LogMessage


class FormatTests(unittest.TestCase):

    def test_date_find(self):
        fmt = 'asd {date_time:%Y} sad {}'
        formatter = LogFormatter(fmt)
        self.assertTrue(formatter.has_date)
        self.assertEqual('%Y', formatter.date_fmt_str)

    def test_format(self):
        test_message = LogMessage('test message', LogLevel.WARNING, 123,
                                  datetime.datetime(2020, 1, 1, 12, 12, 35, 112233))

        formatter1 = LogFormatter('[{thread_id} ]')
        self.assertEqual('[123 ]', formatter1.format(test_message))

        formatter2 = LogFormatter('{AS: {level} }')
        self.assertEqual('{AS: WARNING }', formatter2.format(test_message))

        formatter3 = LogFormatter(' || {date_time:%Y..%d} || ')
        self.assertEqual(' || 2020..01 || ', formatter3.format(test_message))

        formatter4 = LogFormatter('{date_time}  [{level}]: {message}')
        self.assertEqual('2020-01-01 12:12:35.112233  [WARNING]: test message', formatter4.format(test_message))

    def test_manual_log(self):
        cstream = bllog.StreamBuilder().console().color_line().build()
        logger = bllog.LoggerBuilder().name('Test Log').streams([cstream]).build()

        logger.log(LogMessage('Test Message', LogLevel.DEBUG, 112233,datetime.datetime.now()))
        self.assertTrue(True)


if __name__ == '__main__':
    FormatTests().test_manual_log()