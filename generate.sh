#!/bin/sh

rm -rf lightdm/ kitty/ sway/ waybar/ helix/ dunst/ aliases packages

mkdir lightdm

xbps-query -m > packages
cp ~/.bash_aliases aliases
cp /etc/lightdm/lightdm.conf lightdm
cp /etc/lightdm/lightdm-mini-greeter.conf lightdm
cp /etc/lightdm/bg.png lightdm
cp -r ~/.config/kitty kitty
cp -r ~/.config/sway sway
cp -r ~/.config/waybar waybar
cp -r ~/.config/helix helix
cp -r ~/.config/dunst dunst
