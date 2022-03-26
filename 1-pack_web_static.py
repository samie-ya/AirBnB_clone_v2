#!/usr/bin/python3
"""THis script will generate tgz archive from contents of the webstatic"""

from fabric.api import local
from datetime import datetime
import os


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
