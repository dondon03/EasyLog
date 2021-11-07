import inspect
import datetime
import os
from enum import Enum

class LogLevel(Enum):
    TRACE = 10
    DEBUG = 20
    INFO  = 30
    WARN  = 40
    ERROR = 50
    FATAL = 60
    NONE  = 70

class EasyLog:
    def __init__(self, log_level = LogLevel.DEBUG, filename = 'log/LogFile'):
        self.create_dir(filename)
        
        # log file open
        now = datetime.datetime.now()
        filename = filename + now.strftime('_%Y%m%d%H%M%S')+ '.log'
        self.f = open(filename, 'w')

        # log level
        self.log_level = log_level

        # len paramaster
        self.level_len = 8
        self.fn_len = 50
        self.cls_len = 10
        self.fnc_len = 50
        self.no_len = 6

    def __del__(self):
        self.f.close()
        
    def create_dir(self, path):
        dirname = os.path.dirname(path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

    def get_log_str(self, level):
        now = datetime.datetime.now()
        now = now.strftime('%Y/%m/%d %H:%M:%S').ljust(19)
        level = level.ljust(self.level_len)
        fn = inspect.currentframe().f_back.f_back.f_code.co_filename.ljust(self.fn_len)
        cls = inspect.currentframe().f_back.f_back.f_locals.get('self').__class__.__name__.ljust(self.cls_len)
        fnc = inspect.currentframe().f_back.f_back.f_code.co_name
        vars = inspect.currentframe().f_back.f_back.f_code.co_varnames.__str__()
        fnc = (fnc + vars).ljust(self.fnc_len)
        no = str(inspect.currentframe().f_back.f_back.f_lineno).ljust(self.no_len)
        
        log = ('{} [{} : {} : {}@{}@{}] ').format(level, now, fn, cls, fnc, no)
        return log

    def fnc_in(self):
        if (LogLevel.DEBUG.value < self.log_level.value):
            return False
        log = self.get_log_str('IN')+ '\n'
        self.f.write(log)
        return True

    def fnc_out(self):
        if (LogLevel.DEBUG.value < self.log_level.value):
            return False
        log = self.get_log_str('OUT')+ '\n'
        self.f.write(log)
        return True

    def trace(self, message, show = True):
        if (LogLevel.TRACE.value < self.log_level.value):
            return False
        log = ''
        if show:
            log = self.get_log_str('  TRACE')
        log = log + message
        self.f.write(log)
        return True
        
    def debug(self, message, show = True):
        if (LogLevel.DEBUG.value < self.log_level.value):
            return False
        log = ''
        if show:
            log = self.get_log_str('  DEBUG')
        log += message
        self.f.write(log)
        return True

    def info(self, message, show = True):
        if (LogLevel.INFO.value < self.log_level.value):
            return False
        log = ''
        if show:
            log = self.get_log_str('  INFO')
        log += message
        self.f.write(log)
        return True

    def warn(self, message, show = True):
        if (LogLevel.WARN.value < self.log_level.value):
            return False
        log = ''
        if show:
            log = self.get_log_str('  WARN')
        log += message
        self.f.write(log)
        return True

    def error(self, message, show = True):
        if (LogLevel.ERROR.value < self.log_level.value):
            return False
        log = ''
        if show:
            log = self.get_log_str('  ERROR')
        log += message
        self.f.write(log)
        return True

    def fatal(self, message, show = True):
        if (LogLevel.FATAL.value < self.log_level.value):
            return False
        log = ''
        if show:
            log = self.get_log_str('  FATAL')
        log += message
        self.f.write(log)
        return True

logger = EasyLog()