#!/usr/bin/python3
# Generates a .tgz archive from the contents of the web_static folder

from fabric.api import *
from datetime import datetime


def do_pack():
    """do Packs to create a .tgz file"""
    time = datetime.now()
    file_ = 'versions/web_static_{}{}{}{}{}{}.tgz'\
                .format(time.year, time.month, time.day, time.hour, time.minute, time.second)
    local('mkdir -p versions')
    # Compress files using tar:
    # tar -cvzf <name of tarball>.tgz /path/to/source/folder
    compress = local("tar -cvzf " + file_name + " ./web_static/")
    if compress.succeeded:
        return file_
    else:
        return None
