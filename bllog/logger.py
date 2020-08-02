# The main logger implementation
from enum import Enum


class LogLevel(Enum):
    TRACE = 1
    DEBUG = 2
    INFO = 3
    WARNING = 4
    ERROR = 5
    FATAL = 6

class LogMessage():
    """A log message to be written to the streams"""

    # TODO Do actual init
    def __init__(self):
        self.date_time = ""
        self.thread_id = 0
        self.name = ""
        self.level = LogLevel.INFO
        self.message = ""
        self.ex = None

    pass


class Logger():
    pass