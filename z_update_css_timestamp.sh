#!/bin/bash

cd "$(dirname "$0")"

current_time_stamp=$(date +%s)

# Update CSS timestamps
for file in *.css; do
    touch "$file"
done

for file in ./*.html; do
    sed -i "s|<link rel=\"stylesheet\" href=\"styles.css.*\">|<link rel=\"stylesheet\" href=\"styles.css?${current_time_stamp}\">|g" "$file"
done
