#!/usr/bin/python3
"""This function will depoly all the other functions"""

from fabric.api import env
do_pack = __import__('1-pack_web_static').do_pack
do_dep = __import__('2-do_deploy_web_static').do_deploy


env.hosts = ['ubuntu@34.148.148.119', 'ubuntu@44.200.78.83']


def deploy():
    """This will sum up the other functions we created"""
    pack = do_pack()
    if not pack:
        return False
    return do_dep(pack)
