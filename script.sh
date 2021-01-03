tmpfile=$(mktemp)
tmpfile2=$(mktemp)
vowel="аъоуеияю"

while read file; do 
	> "$tmpfile"
	> "$tmpfile2"

	egrep -oi "([а-я]{4,})" "$file" | egrep "^([^$vowel]+[$vowel]*[^$vowel]*[$vowel]*)|^([$vowel]+[^$vowel]*[$vowel]*[^$vowel]*)|^(.{5})" -io | sort -u > "$tmpfile"

	counter=0
	while read word; do
		if grep -q "^$word" $(ls ~/Git/Book-Classifier/noise_data/*); then
			continue
		fi
		echo "$word" | awk '{print tolower($0)}' >> "$tmpfile2"
	done < "$tmpfile"

	sort "$tmpfile2" | uniq -c | sort -rn | head -n 2000 | awk '{print $2}' >> words_per_book
done < "$1"

rm "$tmpfile"
rm "$tmpfile2"
