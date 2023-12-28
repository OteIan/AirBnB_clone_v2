#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

sudo apt-get update
sudo apt install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

echo "Hello There!" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

printf '%s\n' "server {
	listen 80 default_server;
	listen [::]:80 default_server;

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

sudo service nginx restart
