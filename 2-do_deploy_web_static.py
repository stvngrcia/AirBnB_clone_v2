#!/usr/bin/python3
import os
from datetime import datetime
from fabric.api import *


env.hosts = ['34.239.246.45','54.165.80.30']


def do_pack():
    '''
        Creating an archive with the file in web_static folder
    '''
    now = datetime.now()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                             now.month,
                                                             now.day,
                                                             now.hour,
                                                             now.minute,
                                                             now.second)
    print("Packing web_static to versions/{}".format(filename))
    local("mkdir -p versions")
    result = local("tar -vczf {} web_static".format(filename))
    if result.succeeded:
        return (filename)
    else:
        return None


def do_deploy(archive_path):
    '''
        Deploys an archive to the web servers
    '''
    if not os.path.exists(archive_path):
        return False
    result = put(archive_path, "/tmp/")
    if result.failed:
        return False
    result = run("tar -xzvf /tmp/*.tgz -C /data/web_static/releases/ ")
    if result.failed:
        return False
    result = run("rm /tmp/*")
    if result.failed:
        return False
    result = run("rm /data/web_static/current")
    if result.failed:
        return False
    result = run("ln -sf /data/web_static/releases/web_static\
                  /data/web_static/current")
    if result.failed:
        return False
    return True
