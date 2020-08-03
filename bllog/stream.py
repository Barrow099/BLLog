# Output stream for logger

import abc
import os
import sys

import colorama
import termcolor

from bllog.log_classes import LogMessage, LogLevel
from bllog.fomat import LogFormatter


default_format_string = '{date_time:%Y-%m-%d %H:%M:%S.%f} {thread_id} [{level}]: {message}'

default_format = LogFormatter(default_format_string)

class LogStream(abc.ABC):

    def __init__(self):
        self.formatter = default_format
        self.is_open = False

    def set_formatter(self, fmt: LogFormatter):
        self.formatter = fmt

    @abc.abstractmethod
    def init(self):
        """Initialize the stream here. Ex: setup color, open file, rotate, etc"""
        pass

    @abc.abstractmethod
    def destroy(self):
        """Close the stream. Note that this is not always called, the interpreter can crash on
        force closed"""
        pass

    def open(self):
        if not self.is_open:
            self.init()
            self.is_open = True

    def close(self):
        if self.is_open:
            self.destroy()
            self.is_open = False

    def log(self, msg: LogMessage):
        if not self.is_open:
            raise IOError('Stream not open')
        self.write_log(msg)

    @abc.abstractmethod
    def write_log(self, msg: LogMessage):
        """Write log message to output"""
        pass


class ConsoleStream(LogStream):
    def init(self):
        self.line_color = False
        pass

    def destroy(self):
        """Do nothing :D"""
        pass

    def write_log(self, msg: LogMessage):
        p_message = self.formatter.format(msg)

        if self.line_color:
            p_message = color(p_message, msg.level)

        sys.stdout.write(p_message)
        sys.stdout.write(os.linesep)
        sys.stdout.flush()

    def enable_line_color(self, enabled: bool):
        self.line_color = enabled
        if enabled:
            colorama.init()


class StreamBuilder:
    def __init__(self):
        self.proto = None

    def console(self):
        self.proto = ConsoleStream()
        return self

    def color_level(self):
        self.proto.enable_level_color(True)
        return self

    def color_line(self):
        self.proto.enable_line_color(True)
        return self

    def build(self):
        return self.proto


color_map = {
            LogLevel.TRACE: lambda s: termcolor.colored(s, 'grey'),
            LogLevel.DEBUG: lambda s: termcolor.colored(s, 'white'),
            LogLevel.INFO: lambda s: termcolor.colored(s, 'green'),
            LogLevel.WARNING: lambda s: termcolor.colored(s, 'yellow'),
            LogLevel.ERROR: lambda s: termcolor.colored(s, 'red'),
            LogLevel.FATAL: lambda s: termcolor.colored(s, 'red', 'on_white')
}


def color(msg: str, lvl: LogLevel):
    return color_map[lvl](msg)
