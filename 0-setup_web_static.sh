#!/usr/bin/env bash
# This script will sets up your web servers for the deployment of web_static
if ! command -v nginx > /dev/null ;
then
   sudo apt-get update
   sudo apt-get -y install nginx
   sudo ufw --force enable
   sudo ufw allow 'Ngnix HTTP'
fi
if [ ! -d "/data/" ];
then
    sudo mkdir /data/
fi
if [ ! -d "/data/web_static/" ];
then
   sudo mkdir /data/web_static/
fi
if [ ! -d "/data/web_static/releases/" ];
then
    sudo mkdir /data/web_static/releases/
fi
if [ ! -d "/data/web_static/shared/" ];
then
    sudo mkdir /data/web_static/shared/
fi
if [ ! -d "/data/web_static/releases/test/" ];
then
    sudo mkdir /data/web_static/releases/test/
fi
sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
if [ -L "/data/web_static/current" ];
then
    sudo unlink /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i -e "s+:80 default_server;+:80 default_server;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n+" /etc/nginx/sites-available/default
sudo service nginx restart
