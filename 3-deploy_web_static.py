#!/usr/bin/python3
"""This function will depoly all the other functions"""

from fabric.api import env
import os
do_pack = __import__('1-pack_web_static').do_pack
do_depo = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """This will sum up the other functions we created"""
    path = do_pack()
    if not path:
        return False
    else:
        res = do_depo(path)
        return res
