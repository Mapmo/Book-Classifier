#!/bin/bash

tmpfile=$(mktemp)
tmpfile2=$(mktemp)
vowel="аъоуеияю"

while read file; do
    > "$tmpfile"
    > "$tmpfile2"

    egrep -oi "([а-я]{4,})" "$file" | egrep "^([^$vowel]+[$vowel]*[^$vowel]*[$vowel]*)|^([$vowel]+[^$vowel]*[$vowel]*[^$vowel]*)|^(.{5})" -io | sort | uniq -c | sort -rn | head -n 2500 | awk '{print $2}' > "$tmpfile"

    while read word; do
        if grep -q "^$word" $(ls ~/Git/Book-Classifier/noise_data/*); then
            continue
        fi
        echo "$word" | awk '{print tolower($0)}' >> "$tmpfile2"
    done < "$tmpfile"

    head -n 2000 "$tmpfile2" >> words_per_book
done < "$1"

rm "$tmpfile"
rm "$tmpfile2"
