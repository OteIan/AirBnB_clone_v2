#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
from os import path, makedirs
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder"""


def do_pack():
	"""Package the files in form of .tgz"""
	try:
		if not path.exists("versions"):
			makedirs("versions")

		now = datetime.now()
		archive_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year,
                        now.month,
                        now.day,
                        now.hour,
                        now.minute,
                        now.second)
		
		# Compress the files from web_static
		local(f"tar -cvzf versions/{archive_name} web_static")

		return f"versions/{archive_name}"
	except Exception as e:
		print(e)
		return None
