# -*- coding: utf-8 -*-
"""
logging模块
"""

import sys

# reload(sys)
# sys.setdefaultencoding("utf-8")
sys.path.append("../")
import os
import json

import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Handler
from logging.config import dictConfig
import time


class SafeRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False):
        TimedRotatingFileHandler.__init__(self, filename, when, interval, backupCount, encoding, delay, utc)

    """
    重写 doRollover
    lines commanded by "##" is changed by ljt
    """

    def doRollover(self):
        """
        do a rollover; in this case, a date/time stamp is appended to the filename
        when the rollover happens.  However, you want the file to be named for the
        start of the interval, not the current time.  If there is a backup count,
        then we have to get a list of matching filenames, sort them and remove
        the one with the oldest suffix.

        Override,   1. if dfn not exist then do rename
                    2. _open with "a" model
        """
        if self.stream:
            self.stream.close()
            self.stream = None
        # get the time that this sequence started at and make it a TimeTuple
        currentTime = int(time.time())
        dstNow = time.localtime(currentTime)[-1]
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
            dstThen = timeTuple[-1]
            if dstNow != dstThen:
                if dstNow:
                    addend = 3600
                else:
                    addend = -3600
                timeTuple = time.localtime(t + addend)
        dfn = self.baseFilename + "." + time.strftime(self.suffix, timeTuple)
        ##        if os.path.exists(dfn):
        ##            os.remove(dfn)

        # Issue 18940: A file may not have been created if delay is True.
        ##        if os.path.exists(self.baseFilename):
        if not os.path.exists(dfn) and os.path.exists(self.baseFilename):
            os.rename(self.baseFilename, dfn)
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)
        if not self.delay:
            self.mode = "a"
            self.stream = self._open()
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        # If DST changes and midnight or weekly rollover, adjust for this.
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                    addend = -3600
                else:  # DST bows out before next rollover, so we need to add an hour
                    addend = 3600
                newRolloverAt += addend
        self.rolloverAt = newRolloverAt


# ----------------------------------------------------------------------------------------------------------------------
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

fmt = '%(asctime)s (%(process)d) [%(filename)s-%(module)s-%(funcName)s %(lineno)d] %(levelname)s: %(message)s'

# 输出格式  时间 （进程号） [文件名-模块名-函数名-行号] 日志等级:日志

fmt_db = '%(name)s|_|%(asctime)s|_|%(process)d|_|%(filename)s|_|%(module)s|_|%(funcName)s|_|%(lineno)d|_|%(levelname)s|_|%(levelno)s|_|%(message)s'
level_config = {
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARN': logging.WARNING,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
    'NOTSET': logging.NOTSET,
}

path1 = 'Config.ini'
# path2 = 'ConfigLog.ini'

config = {
    'file_level': 'INFO',
    'debug': 'false',
    'stream_level': 'INFO',
    'type': 'kafka',
    'db_level': 'INFO',
    'logger_level': 'INFO'
}


class Logging1(object):
    """
    logging日志类
    use eg:
    log = Logging(name = 'anhui,level = logging.INFO).getLogger
    log.info(u'爬虫抓取开始')
    """

    def __init__(self, name=None, file_flag=None, db_flag=None, stream_flag=True, log_type=None):
        assert name is not None, 'name == None'
        self.name = name.lower()
        self.log_type = log_type

        self.pid = os.getpid()
        if stream_flag:
            self.stream_flag = stream_flag
        else:
            self.stream_flag = None
        if file_flag:
            self.file_flag = file_flag
        else:
            self.file_flag = True
        # .getLogger 调用日志接口
        self.logger = logging.getLogger(self.name)
        self.cf = config
        # 初始化logger
        self.logger.setLevel(level_config[self.cf['logger_level']])
        # 设置logger等级
        self.getLogger()
        self.logger.propagate = False

    def getLogger(self):
        if self.logger.handlers:
            return self.logger
        if self.stream_flag:
            sl = self.streamLogger()
            self.logger.addHandler(sl)
        # if self.cf['debug'] == 'true':
        #     return self.logger
        if self.file_flag:
            fl = self.fileLogger()
            self.logger.addHandler(fl)

        return self.logger

    def fileLogger(self):
        """
        日志输出到文件
        :return:
        """
        log_env = os.getenv('spider_log', default=None)
        if log_env:
            filename = os.path.join(log_env, self.name + '_' + str(self.pid))
        else:
            filename = self.name
        if self.log_type:
            filename += "_" + self.log_type
        filehandler = SafeRotatingFileHandler(filename, 'D', 1, 2)
        filehandler.suffix = '%Y-%m-%d.log'
        filehandler.setLevel(level_config[self.cf['file_level']])
        fmtr = logging.Formatter(fmt=fmt)
        filehandler.setFormatter(fmtr)
        return filehandler

    def streamLogger(self):
        """
        日志输出到屏幕
        :return:
        """

        sl = logging.StreamHandler()
        sl.setLevel(level_config[self.cf['stream_level']])
        fmtr = logging.Formatter(fmt=fmt)
        sl.setFormatter(fmtr)
        return sl


class Logging2(Logging1):
    pass


def Logging(name=None, **kw):
    log = Logging1(name, **kw)
    return log.logger


def LogingMain(name=None, **kw):
    log = Logging2(name, **kw)
    return log.logger


if __name__ == '__main__':
    # log1 = Logging(name='test1')
    # print log1
    # log.getLogger.info('eg msg')
    # logger11 = logging.getLogger("11")
    # logger12 = logging.getLogger("12")
    log2 = Logging(name='test2', file_flag=True, stream_flag=True, db_flag=True)
    log2.info(u'测试logging')
    log2 = Logging(name='test2', file_flag=True, stream_flag=True, db_flag=True)
    log2.info(u'测试logging')
    # logger13 = logging.getLogger("13")
    # log3 = LogingMain(name = 'test2', file_flag = True, stream_flag = False)
    # print(log3)
    # log3.info('adddress =%s ', str(log2))
