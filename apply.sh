#!/usr/bin/bash

cp aliases ~/.bash_aliases
sudo cp -a lightdm/. /etc/lightdm
cp -a kitty/. ~/.config/kitty
cp -a sway/. ~/.config/sway
cp -a waybar/. ~/.config/waybar
cp -a helix/. ~/.config/helix
cp -a dunst/. ~/.config/dunst
chmod +x ~/.startup
chmod +x ~/.bash_aliases
