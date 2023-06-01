#!/bin/bash
# install flathub
sudo add-apt-repository ppa:flatpak/stable
sudo apt update
sudo apt install flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
# for gnoeme-software 
sudo apt install gnome-software-plugin-flatpak
# for KDE discover
sudo apt install plasma-discover-backend-flatpak


