#!/usr/bin/bash

rm aliases 2> /dev/null
rm -r lightdm 2> /dev/null
rm -r kitty 2> /dev/null
rm -r sway 2> /dev/null
rm -r waybar 2> /dev/null
rm -r helix 2> /dev/null
rm -r dunst 2> /dev/null

mkdir lightdm

cp ~/.bash_aliases aliases
cp /etc/lightdm/lightdm.conf lightdm
cp /etc/lightdm/lightdm-mini-greeter.conf lightdm
cp /etc/lightdm/bg.png lightdm
cp -r ~/.config/kitty kitty
cp -r ~/.config/sway sway
cp -r ~/.config/waybar waybar
cp -r ~/.config/helix helix
cp -r ~/.config/dunst dunst
