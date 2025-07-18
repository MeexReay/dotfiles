#!/bin/bash

now_delta="$(brightnessctl get)"
delta="$(python -c "print(max(0, min(255, $now_delta + int($1 / 100 * 255))))")"
iter="$(python -c "print(-1 if $1 < 0 else 1)")"

for i in $(seq $now_delta $iter $delta)
do
  if [ $iter == -1 && $(brightnessctl get) < $i ]
  then
    break
  fi

  if [ $iter == 1 && $(brightnessctl get) > $i ]
  then
    break
  fi

  brightnessctl set $i
  sleep 0.01s
done
