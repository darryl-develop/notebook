# Rpi3 Server
[*plex*](#plex) | [*sabnzbd*](#sabnzbd) | [*pi hole*](#pi-hole)

###### Base Install
- [Raspbian](https://downloads.raspberrypi.org/raspbian_lite_latest)
  - [wpa_supplicant.conf](/boot/wpa_supplicant.conf)
  - [ssh](/boot/ssh)
- *Update Hostname*
- *Set GPU Memory to 16*

###### Create User
```bash
sudo useradd -m -g sudo plex
sudo useradd -m -g sudo sabnzbd
sudo useradd -m -g sudo pihole

sudo passwd plex
sudo passwd sabnzbd
sudo passwd pihole

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
su - plex

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
su - sabnzbd

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

# Pi Hole {t}
###### Install | [*web*](http://pi.hole/admin)
```bash
su - pihole

curl -sSL https://install.pi-hole.net | bash
```
- [Configure Router DNS Server](https://discourse.pi-hole.net/t/how-do-i-configure-my-devices-to-use-pi-hole-as-their-dns-server/245)
