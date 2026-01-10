#!/usr/bin/env bash

WALLDIR="$HOME/wallpaper"

while true; do
  feh --bg-scale --randomize --nofehbg "$WALLDIR"/* 2>/dev/null
  sleep 120
done
