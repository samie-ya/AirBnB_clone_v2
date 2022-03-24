#!/usr/bin/python3
"""This function will depoly all the other functions"""
from fabric.api import *
from fabric.operations import run, put
from datetime import datetime
import os

env.hosts = ['ubuntu@34.148.148.119', 'ubuntu@44.200.78.83']


def do_pack():
    """This function will create the archive"""
    today = datetime.now()
    if not os.path.exists("versions"):
        local("mkdir versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static"
              .format(today.strftime("%Y%m%d%H%M%S")))
        if ("versions/web_static_{}.tgz"
           .format(today.strftime("%Y%m%d%H%M%S"))):
            return ("versions/web_static_{}.tgz"
                    .format(today.strftime("%Y%m%d%H%M%S")))
        else:
            return None
    else:
        local("tar -cvzf versions/web_static_{}.tgz web_static"
              .format(today.strftime("%Y%m%d%H%M%S")))
        if ("versions/web_static_{}.tgz"
           .format(today.strftime("%Y%m%d%H%M%S"))):
            return ("versions/web_static_{}.tgz"
                    .format(today.strftime("%Y%m%d%H%M%S")))
        else:
            return None


def do_deploy(archive_path):
    """This function will depoly archives"""
    if os.path.exists(archive_path):
        value = archive_path.split('/')[1]
        new = value.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(new))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(value, new))
        run("rm /tmp/{}".format(value))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(new, new))
        run("rm -rf /data/web_static/releases/{}/web_static/".format(new))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(new))
        return True
    else:
        retun False


def deploy():
    """This will sum up the other functions we created"""
    pack = do_pack()
    if not pack:
        return False
    return do_dep(pack)
