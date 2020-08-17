#!/usr/bin/python3
"""files compression"""

from datetime import datetime
from fabric.api import run, put, local


def do_pack():
    """compress file"""
    day = datetime.today()
    path = "versions/web_static_{}.tgz".format(day.isoformat())
    if local("mkdir -p versions; tar -vfzc {} web_static".format(path)):
        return path
    else:
        return None
