from bllog.logger import Logger, LogLevel
from bllog.fomat import LogFormatter

default_format_string = '{date_time:%Y-%m-%d %H:%M:%S.%f} {thread_id} [{level}]: {message}'

default_format = LogFormatter(default_format_string)

def get_default_formatter():
    return default_format