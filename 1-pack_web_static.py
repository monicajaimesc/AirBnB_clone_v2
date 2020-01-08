#!/usr/bin/python3
# Generates a .tgz archive from the contents of the web_static folder

from datetime import datetime
from fabric.api import local


def do_pack():
    """do Packs to create a .tgz file"""
    t = datetime.now()
    file_ = 'versions/web_static_{}{}{}{}{}{}.tgz'\
            .format(t.year, t.month, t.day, t.hour, t.minute, t.second)
    local('mkdir -p versions')
    # Compress files using tar:
    # tar -cvzf <name of tarball>.tgz /path/to/source/folder
    compress = local("tar -cvzf " + file_ + " ./web_static/")
    if compress.succeeded:
        return file_
    else:
        return None
