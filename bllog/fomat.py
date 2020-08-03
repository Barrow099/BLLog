# Log message formatting
import datetime

from bllog.logger import LogMessage

# '{date_time:%Y-%m-%d %H:%M:%S.%f} {thread_id} [{level}]: {message}'
class LogFormatter():

    # TODO Document format
    def __init__(self, fmt: str):
        self.parse_format(fmt)
        self.format_string = fmt

    def parse_format(self, fmt: str):

        self.parse_date(fmt)

        pass

    def format(self, msg: LogMessage):
        r_mesg = self.format_string

        r_mesg = r_mesg.replace('{thread_id}', str(msg.thread_id))
        r_mesg = r_mesg.replace('{level}', msg.level.name)
        r_mesg = r_mesg.replace('{message}', msg.message)
        r_mesg = r_mesg.replace('{name}', msg.name)

        if self.has_date:
            start = r_mesg.find('{date_time')
            end = find_endpos(r_mesg, start)
            r_mesg = r_mesg[:start ] + msg.date_time.strftime(self.date_fmt_str) + r_mesg[end + 1:]

        return r_mesg

    def parse_date(self, fmt: str):
        try:
            loc = fmt.index('{date_time')
            endpos = find_endpos(fmt, loc)

            date_string = fmt[loc + 1: endpos]
            if ':' in date_string:
                date_format = date_string[date_string.find(':') + 1:]
            else:
                date_format = '%Y-%m-%d %H:%M:%S.%f'
            self.has_date = True
            self.date_fmt_str = date_format

        except ValueError:
            # Not found
            self.has_date = False
            self.date_fmt_str = ''


def find_endpos(msg: str, start: int):
    """Finds the closing } for a open one"""
    lvl = 0
    for i in range(start + 1, len(msg) - 1):
        char = msg[i]
        if char == '{':
            lvl += 1
        elif char == '}':
            if lvl > 0:
                lvl -= 1
            else:
                return i
    raise ValueError('No closing } found')
