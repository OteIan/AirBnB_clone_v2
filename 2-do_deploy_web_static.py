#!/usr/bin/python3
"""Fabric script that distributes an archive to the web servers"""


def do_deploy(archive_path):
	"""Distributes an archive to the web servers"""
	from fabric.api import put, run, env
	from os.path import exists
	env.hosts = ["3.84.158.65 335371-web-01", "3.90.85.11 335371-web-02"]
	env.user = "ubuntu"
	env.private_key_filename = "~/.ssh/school"

	if not exists(archive_path):
		return False
	
	try:
		# Upload the archive to /tmp/ dir on the server
		put(archive_path, '/tmp/')

		# Uncommpress the archive to the folder /data/web_static/releases/
		filename = archive_path.split('/')[-1]
		release_path = '/data/web_static/releases/{}'.format(filename.split('.')[0])
		run('mkdir -p {}'.format(release_path))
		run('tar -xzf /tmp/{} -C {}'.format(filename, release_path))
		
		# Delete the archive from the web server
		run('rm /tmp/{}'.format(archive_path))

		# Delete the symbolic link /data/web_static/current from the web server
		run('rm -f /data/web_static/current')

		# Create a new the symbolic link /data/web_static/current on the web server
		run('ln -s {} /data/web_static/current'.format(release_path))
		
		print('New version deployed!')
		return True
	except Exception as e:
		print(e)
		return False