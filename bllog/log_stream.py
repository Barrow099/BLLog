# Output stream for logger

import abc

from bllog.logger import LogMessage


class LogStream(abc.ABC):

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
        pass
