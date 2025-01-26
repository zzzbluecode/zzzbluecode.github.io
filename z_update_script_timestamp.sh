#!/bin/bash

cd "$(dirname "$0")"

current_time_stamp=$(date +%s)

echo "Updating script.js timestamp..."
sed -i "s|fetch('left-panel.html.*)|fetch('left-panel.html?t=${current_time_stamp}')|" ./script.js