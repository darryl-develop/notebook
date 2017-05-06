# Rpi3 Server
[*plex*](#plex) | [*sabnzbd*](#sabnzbd)

###### Base Install
- [Raspbian](https://downloads.raspberrypi.org/raspbian_lite_latest)
  - [wpa_supplicant.conf](/boot/wpa_supplicant.conf)
  - [ssh](/boot/ssh)
- *Update Hostname*
- *Set GPU Memory to 16*

###### Create User
```bash
sudo useradd -m -g rpi3
sudo passwd rpi3
sudo reboot
```
```bash
sudo userdel pi
cd /home
sudo rm -rf pi
```


# Plex
###### Install | [*web*](http://localhost:32400/)
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade

sudo reboot

sudo apt-get install apt-transport-https

cd /etc/apt
sudo nano sources.list
 - deb https://dev2day.de/pms/ jessie main

wget -O - https://dev2day.de/pms/dev2day-pms.gpg.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install -t jessie plexmediaserver

sudo reboot
```

###### Mount Storage
```bash
sudo fdisk -l
sudo mkdir media
sudo nano /etc/fstab
 - /dev/sda1 /media vfat defaults 0 0
```




# Sabnzbd {t}
###### Install | [*web*](http://localhost:5050)
```bash
sudo apt-get install sabnzbdplus
```

###### CouchPotato | [*web*](http://localhost:5050/)
```bash
sudo apt-get install git-core
sudo mkdir plugin
cd /plugin

git clone git clone https://github.com/CouchPotato/CouchPotatoServer.git
sudo cp CouchPotatoServer/init/ubuntu /etc/init.d/couchpotato
sudo chmod +x /etc/init.d/couchpotato
sudo update-rc.d couchpotato defaults
```
