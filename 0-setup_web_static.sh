#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

apt-get update -y
apt-get install nginx -y
ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/{releases/test,shared}
# the file wile contain: 
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
# ln to create a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
