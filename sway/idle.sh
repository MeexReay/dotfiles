#!/bin/bash

LOCK_CMD="swaylock -f --color 000000"

swayidle -w \
    timeout 600 "$LOCK_CMD" \
    timeout 1200 'sudo zzz' \
    before-sleep "$LOCK_CMD" \

