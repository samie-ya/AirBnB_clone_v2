#!/usr/bin/python3
"""This script will distribute archive in webserver"""

from fabric.api import *
from fabric.operations import run, put
import os

env.hosts = ['ubuntu@34.148.148.119', 'ubuntu@44.200.78.83']


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
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(new, new))
        run("rm -rf /data/web_static/releases/{}/web_static/".format(new))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(new))
        return True
    else:
        return False
