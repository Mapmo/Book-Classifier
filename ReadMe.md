Sources:
<ul>
	<li> noise_data:
		<ul>
			<li> city_names: https://datahub.io/core/world-cities#data </li>
			<li> country_names: https://bg.wikipedia.org/wiki/%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BB:%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D0%B5_%D0%B2_%D1%81%D0%B2%D0%B5%D1%82%D0%B0 </li>
			<li> human_names: http://www.nrscotland.gov.uk/files/statistics/pop-names-07-t4.csv</li>
		</ul>
	</li>
</ul>

Current Idea:
ls \*txt > all
split -n l/4 all
for i in $(ls xa\*); do
	script.sh "$i" &
done

sort words_per_book | uniq -c | sort -rn | awk '{if ($1 > 5) print $2}' > genre_words
