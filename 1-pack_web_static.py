#!/usr/bin/python3
# Generates a .tgz archive from the contents of the web_static folder

from fabric.api import *
from datetime import datetime

x = datetime.now()


def do_pack():
    """Packs web_static files into .tgz file"""

    file_name = 'versions/web_static_{}{}{}{}{}{}.tgz'\
                .format(x.year, x.month, x.day, x.hour, x.minute, x.second)
    local('mkdir -p versions')
    # Compress files using tar:
    # tar -cvzf <name of tarball>.tgz /path/to/source/folder
    command = local("tar -cvzf " + file_name + " ./web_static/")
    if command.succeeded:
        return file_name
    else:
        return None
