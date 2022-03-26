# This script will set up web static
exec { 'setup web static':
  command  => 'sudo apt-get update; sudo apt-get -y install nginx; sudo ufw --force enable; sudo ufw allow "Nginx HTTP"; sudo mkdir /data/; sudo mkdir /data/web_static/; sudo mkdir /data/web_static/releases/; sudo mkdir /data/web_static/shared/; sudo mkdir /data/web_static/releases/test/; printf "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n" | sudo tee /data/web_static/releases/test/index.html > /dev/null; sudo unlink /data/web_static/current; sudo ln -s /data/web_static/releases/test /data/web_static/current; sudo chown -R ubuntu:ubuntu /data/; sudo sed -ie "0,/location \/ {/s/location \/ {/location \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;/" /etc/nginx/sites-available/default; sudo service nginx restart',
  provider => shell,
}
