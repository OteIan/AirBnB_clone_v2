#!/usr/bin/python3
from fabric.api import local, env, put, run
from datetime import datetime
from os import path, makedirs
"""Distributes an archive to the web servers"""


env.hosts = ['100.25.131.49', '52.3.250.251']


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

        a, b = archive_name, archive_size

        print(f"web_static packed: versions/{a} -> {b}Bytes")

        return (f"versions/{archive_name}")

    except Exception as e:
        print(e)
        return None


def do_deploy(archive_path):
    """Distributes an archive to a web server"""
    if not path.exists(archive_path):
        return False

    try:
        # Upload the archive into /tmp/ on the server
        put(archive_path, '/tmp/')

        # Uncompress the archive to the folder /data/web_static/releases/
        archive_name = archive_path.split('/')[-1]
        destination = f"/data/web_static/releases/{archive_name.split('.')[0]}"
        run(f"mkdir -p {destination}")
        run(f"tar -xzf /tmp/{archive_name} -C {destination}")

        # Delete the archive from the web server
        run(f"rm -rf /tmp/{archive_path}")
        run(f"mv {destination}/web_static/* {destination}")

        # Delete the web_static folder from the web_server
        run(f"rm -rf {destination}/web_static")
        run(f"rm -rf /data/web_static/current")

        # Create a symbolic link pointing to /data/web_static/current
        run(f"ln -s {destination} /data/web_static/current")

        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False
