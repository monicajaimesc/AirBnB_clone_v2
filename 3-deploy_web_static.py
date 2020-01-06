#!/usr/bin/python3
"""
Creates and distributes an archive to web servers
"""
from fabric.api import *
from os import path
from datetime import datetime

# do_pack = __import__('1-pack_web_static').do_pack
# do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['35.243.170.219', '35.237.154.254']
env.user = 'ubuntu'

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


def do_deploy(archive_path):
    """Deploys path of the archive"""
    if not path.exists(archive_path):
        return False
    value = True
    # put asks the connection cache for a connection to the servers;
    a_upload_archive = put(archive_path, '/tmp/')
    if a_upload_archive.failed:
        value = False
    archive = archive_path.replace(".tgz", "").replace("versions/", "")
    b_uncompress = run('mkdir -p /data/web_static/releases/' + archive + '/')
    if b_uncompress.failed:
        value = False
    b_uncompress_created = run('tar -xzf /tmp/' + archive
                               + '.tgz' + ' -C /data/web_static/releases/'
                               + archive + '/')
    if b_uncompress_created.failed:
        value = False
    delete_arch = run('rm /tmp/' + archive + '.tgz')
    if delete_arch.failed:
        value = False
    e = run('mv /data/web_static/releases/' + archive +
            '/web_static/* /data/web_static/releases/' + archive + '/')
    if e.failed:
        value = False
    delete_symbolic_link = run('rm -rf /data/web_static/releases/'
                               + archive + '/web_static')
    if delete_symbolic_link.failed:
        value = False
    g = run('rm -rf /data/web_static/current')
    if g.failed:
        value = False
    h = run('ln -sf /data/web_static/releases/' + archive +
            '/' + ' /data/web_static/current')
    if h.failed:
        value = False
    if value:
        print("New version deployed!")
    return value


def deploy():
    """creates and distributes an archive to all servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
