#!/usr/bin/env bash
# Creating server configuration
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "Hello holberton" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i "38i\ \tlocation \/hbnb_static {\\n\\t\\talias \/data\/web_static\/current\/;\\n}" /etc/nginx/sites-available/default
sudo service nginx restart
