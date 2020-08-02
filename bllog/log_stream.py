# Output stream for logger

import abc
import os
import sys

import bllog
from bllog import LogFormatter
from bllog.logger import LogMessage


class LogStream(abc.ABC):

    def __init__(self):
        self.formatter = bllog.get_default_formatter()

    def set_formatter(self, fmt: LogFormatter):
        self.formatter = fmt

    @abc.abstractmethod
    def init(self):
        """Initialize the stream here. Ex: setup color, open file, rotate, etc"""
        pass

    @abc.abstractmethod
    def close(self):
        """Close the stream. Note that this is not always called, the interpreter can crash on
        force closed"""
        pass

    @abc.abstractmethod
    def write_log(self, msg: LogMessage):
        """Write log message to output"""
        pass

class ConsoleStream(LogStream):
    def init(self):
        """Do nothing :D"""
        pass

    def close(self):
        """Do nothing :D"""
        pass

    def write_log(self, msg: LogMessage):
        p_message = self.formatter.format(msg)
        sys.stdout.write(p_message)
        sys.stdout.write(os.linesep)
        sys.stdout.flush()