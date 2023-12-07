#!/usr/bin/env bash
# Prepare my servers for the deployement process

# Install nginx if not installed
sudo apt-get update
sudo apt-get -y  install nginx

# Create the location for various folders and give ownership
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

# Create a fake file to test
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >  /data/web_static/releases/test/index.html

# Create a symlink 
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Configure Nginx
printf '%s\n' "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	# Add a custom header
	add_header X-Served-By \$hostname;

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	
	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}
	
	error_page 404 /404.html;
	
	location = /404.html{
		internal;
	}

	location /hbnb_static {
		alias /data/web_static/current/;
	}
}" | sudo tee /etc/nginx/sites-available/default > /dev/null

# Restart Nginx
sudo service nginx restart
