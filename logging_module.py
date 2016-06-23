#!/usr/bin/env python

import logging


#日志文件输出
# logging.basicConfig(filename="log.log",format="%(asctime)s %(name)s %(levelname)s %(message)s", level=logging.INFO)


#日志记录多输出
logger = logging.getLogger("atm")  #设置logger用户(name)
logger.setLevel(logging.DEBUG)      #设置日志级别

ch = logging.StreamHandler()  #设置控制台日志流句柄
ch.setLevel(logging.INFO)

fh = logging.FileHandler(filename="log1.log")  #设置日志文件名
fh.setLevel(logging.INFO)

LogFomat = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")  #设置文件记录的格式

#既在文件中记录日志也在控制台输出日志
ch.setFormatter(LogFomat)
fh.setFormatter(LogFomat)
logger.addHandler(ch)
logger.addHandler(fh)

logger.info("this is a info")
logger.debug("this is a debug message")
logger.warning("test")
logger.critical("testsdfasdfsadf")
