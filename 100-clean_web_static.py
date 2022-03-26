#!/usr/bin/python3
"""This function will delete the old archives"""
from fabric.api import *
from fabric.operations import *

env.hosts = ['ubuntu@34.148.148.119', 'ubuntu@44.200.78.83']


def do_clean(number=0):
    """This function will delete archives"""
    local("cd versions/ && rm $(ls -t | awk 'NR>{}')"
          .format(number))
    run("cd /data/web_static/releases && rm -rf $(ls -t | awk 'NR>{}')"
        .format(number))
