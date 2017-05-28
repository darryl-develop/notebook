#!/bin/sh

cd
apt-get install python
apt-get install python-cheetah
apt-get install ntfs-3g

git clone https://github.com/sabnzbd/sabnzbd.git
wget -O plex-media-server.deb https://downloads.plex.tv/plex-media-server/1.5.6.3790-4613ce077/plexmediaserver_1.5.6.3790-4613ce077_amd64.deb

dpkg -i plex-media-server.deb
cd sabnzbd
python SABnzbd.py -d --server 0.0.0.0

rm -rf plex-media-server.deb


blkid
echo 'Enter USB Storage UUID from Above: '; read usbUUID
read 'UUID='$usbUUID' /home/plex/media ntfs defaults 0 0'

mkdir /home/plex/media
nano /etc/fstab