#!/bin/bash

dunst &
copyq &
blueman-applet &
~/.config/sway/random-bg.py loop &
~/.startup &

wait
