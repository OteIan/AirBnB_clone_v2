#!/usr/bin/python3
from fabric.api import put, run, env
from os.path import exists
"""Fabric script that distributes an archive to the web servers"""


env.hosts = ["3.84.158.65", "3.90.85.11"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"

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

		# Get the size of the created archive
		archive_size = path.getsize("versions/{}".format(archive_name))

        # Print a message with the packed file and its size
		print("web_static packed: versions/{} -> {}Bytes".format(archive_name, archive_size))

		return "versions/{}".format(archive_name)
	except Exception as e:
		print(e)
		return None
	
def do_deploy(archive_path):
	"""Distributes an archive to the web servers"""
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
		run('rm -f /tmp/{}'.format(archive_path))

		# Move the content of web_static/releases/<archive filename without extension> to
		run('mv {}/web_static/* {}'.format(release_path, release_path))

		# Delete the folder web_static from the web server
		run('rm -rf {}/web_static'.format(release_path))

		# Delete the symbolic link /data/web_static/current from the web server
		run('rm -rf /data/web_static/current')

		# Create a new the symbolic link /data/web_static/current on the web server
		run('ln -s {} /data/web_static/current'.format(release_path))
		
		print('New version deployed!')
		return True
	except Exception as e:
		print(e)
		return False

def deploy():
	"""Creates and distributes an archive to the web servers"""
	try:
		archive_path = do_pack()
		return do_deploy(archive_path)
	except Exception as e:
		print(e)
		return False