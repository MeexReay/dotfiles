#!/usr/bin/bash

cp startup ~/.startup
cp aliases ~/.bash_aliases
cp -a lightdm/. /etc/lightdm
cp -a kitty/. ~/.config/kitty
cp -a sway/. ~/.config/sway
cp -a waybar/. ~/.config/waybar
cp -a helix/. ~/.config/helix
cp -a dunst/. ~/.config/dunst
chmod +x ~/.startup.sh
chmod +x ~/.bash_aliases
