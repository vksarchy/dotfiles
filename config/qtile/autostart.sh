#!/usr/bin/env bash

# 🚫 Exit unless Qtile is running
if ! pgrep -x qtile >/dev/null; then
  exit 0
fi

COLORSCHEME=doom-one

### AUTOSTART PROGRAMS ###

# Compositor (needed for transparency)
picom --daemon &

# AppIndicator → XEmbed bridge (MUST be before tray apps)
snixembed --fork &

dunst -conf "$HOME"/.config/dunst/"$COLORSCHEME" &
nm-applet &
sleep 2

# VPN (Surfshark)
pgrep -x surfshark >/dev/null || surfshark connect &

systemctl --user start mpd &

"$HOME"/.screenlayout/layout.sh &

sleep 1
conky -c "$HOME"/.config/conky/qtile/01/"$COLORSCHEME".conf || echo "Couldn't start conky."

sleep 1
yes | /usr/bin/emacs --daemon &
waypaper --restore &

# Tray app (SafeEyes) — AFTER snixembed
safeeyes &

#"$HOME"/.config/kanata-tray-linux &

if [ ! -d "$HOME/.cache/betterlockscreen" ]; then
  betterlockscreen -u "$HOME/Pictures/wallpaper/astronaut_jellyfish.jpg" &
fi
