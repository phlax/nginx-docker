
import os

import socket
import time

import ngx


def access(r):
    r.log('I was accessed!', ngx.LOG_CRIT)


def content(r):
    r.status = 200
    r.sendHeader()
    r.log('And i responded!', ngx.LOG_CRIT)
    r.send('Hello, world', ngx.SEND_LAST)
