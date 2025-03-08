# My config files

## About

OS: Void Linux x86_64 \
WM: Sway \
Shell: Bash \
Notifications: Dunst \
Terminal Emulator: Kitty \
Bar: Waybar \
Text Editor: Helix \
DM: LightDM + LightdmMiniGreeter \
File Manager: PCManFM

## Screenshots

![image](https://github.com/user-attachments/assets/a408db32-0c0c-4df9-8bd0-9e1b33b37d1a)

## How to install

```bash
sudo ./install.sh # install required packages
./apply.sh # apply configs without lightdm
sudo ./apply.sh # apply configs + lightdm
./generate.sh # copy configs from system
```

### About applying

My username is `user`, so if you want to use my configs with another username, you need to change it from `user` to yours here:
```
lightdm/lightdm-mini-greeter.conf (line: 7)
sway/config (line: 306)
```
