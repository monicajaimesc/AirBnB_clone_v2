#!/usr/bin/python3
# Creates and distributes an archive to web servers

from fabric.api import *
from os import path

env.hosts = ['35.243.170.219', '35.237.154.254']
# fabric will perform in both servers all the functions from here


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
    b_uncompress_created = run('tar -xzf /tmp/' + archive + '.tgz' +
            ' -C /data/web_static/releases/' + archive + '/')
    if b_uncompress_created.failed:
        value = False
    delete_arch = run('rm /tmp/' + archive + '.tgz')
    if delete_arch.failed:
        value = False
    e = run('mv /data/web_static/releases/' + archive +
            '/web_static/* /data/web_static/releases/' + archive + '/')
    if e.failed:
        value = False
    delete_symbolic_link = run('rm -rf /data/web_static/releases/' + archive + '/web_static')
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
