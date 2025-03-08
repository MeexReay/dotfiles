#!/usr/bin/bash

rm aliases 2> /dev/null
rm -r kitty 2> /dev/null
rm -r sway 2> /dev/null
rm -r waybar 2> /dev/null
rm -r helix 2> /dev/null
rm -r dunstrc 2> /dev/null

cp ~/.bash_aliases aliases
cp -r ~/.config/kitty kitty
cp -r ~/.config/sway sway
cp -r ~/.config/waybar waybar
cp -r ~/.config/helix helix
cp -r ~/.config/dunst dunst
