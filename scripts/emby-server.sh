#!/bin/sh

echo "deb http://download.webmin.com/download/repository sarge contrib" | sudo tee -a /etc/apt/sources.list
echo "deb http://download.opensuse.org/repositories/home:/emby/xUbuntu_16.04/ /" | sudo tee -a /etc/apt/sources.list.d/emby-server.list

sudo wget http://www.webmin.com/jcameron-key.asc
sudo apt-key add jcameron-key.asc
wget -nv http://download.opensuse.org/repositories/home:emby/xUbuntu_16.04/Release.key -O Release.key
sudo apt-key add - < Release.key

sudo apt-get update

sudo apt-get install webmin
sudo apt-get install emby-server