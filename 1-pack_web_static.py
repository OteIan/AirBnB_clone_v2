#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
from os import path, makedirs
"""Generates a .tgs archive from the contents of the web_static folder"""


def do_pack():
    """Function that generates the .tgz archive"""
    try:
        if not path.exists("versions"):
            makedirs("versions")

        now = datetime.now()
        archive_name = f"web_static_{now.year}{now.month}{now.day}{now.hour}"
        archive_name += f"{now.minute}{now.second}.tgz"

        local(f"tar -czvf versions/{archive_name} web_static")

        archive_size = path.getsize(f"versions/{archive_name}")

        print(f"web_static packed: versions/{archive_name} -> {archive_size}Bytes")

        return (f"versions/{archive_name}")

    except Exception as e:
        print(e)
        return None
