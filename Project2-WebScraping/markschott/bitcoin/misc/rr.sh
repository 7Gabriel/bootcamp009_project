#!/bin/bash
i=0
while IFS='' read -r line || [[ -n "$line" ]]; do
    echo $i >> check.txt
    i=$((i+1))
    echo "Curling from url: $line"
    echo '[' >> "$2"
    curl $line | grep "<p>.*</p>" ptest.txt | sed 's/<p>//g' | sed 's/<\/p>//g' >> "$2"
    echo '],' >> "$2"
 
done < "$1"
