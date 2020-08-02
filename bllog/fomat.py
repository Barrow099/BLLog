# Log message formatting
from bllog.logger import LogMessage


class LogFormatter():

    # TODO Document format
    def __init__(self, fmt: str):
        self.parse_format(fmt)

    def parse_format(self, fmt: str):

        self.parse_date(fmt)

        pass

    def format(self, msg: LogMessage):
        pass

    def parse_date(self, fmt):
        loc = fmt.index('{date_time')

