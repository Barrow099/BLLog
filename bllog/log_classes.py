from datetime import datetime
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
    def __init__(self, message: str, lvl: LogLevel, tid: int, date_time: datetime):
        self.date_time: datetime = date_time
        self.thread_id = tid
        self.name = ""
        self.level = lvl
        self.message = message
        self.ex = None

    pass