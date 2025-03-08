#!/usr/bin/bash

xbps-install lightdm lightdm-mini-greeter Waybar wayland wlroots \
  sway dunst helix bash kitty pavucontrol wpa-cute blueman \
  make libX11 libX11-devel libXinerama libXinerama-devel \
  fontconfig fontconfig-devel libXft libXft-devel make

cd dmenu
make clean install
