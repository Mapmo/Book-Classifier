Sources:
<ul>
	<li> noise_data:
		<ul>
			<li> <a href="https://datahub.io/core/world-cities#data">city_names</a> </li>
			<li> <a href="https://bg.wikipedia.org/wiki/%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BB:%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D0%B5_%D0%B2_%D1%81%D0%B2%D0%B5%D1%82%D0%B0">country_names</a> </li>
			<li> <a href="http://www.nrscotland.gov.uk/files/statistics/pop-names-07-t4.csv">human_names</a></li>
		</ul>
	</li>
</ul>

How the project works:
<ul>
	<li> extract.py - generates a dataset in JSON format from the most common words in each book </li>
	<li> classify.py - using a specified dataset, created by extract.py, it classifies the genre(s) of a book after learning on the provided dataset </li>
</ul>

Usage:<br>
extract.py
<ul>
	<li> You must be located in a directory that contains other directories named after their genres </li>
	<li> The script will be looking for a txt directory for each genre. This is useful in case you want to have zip files for the books in each genre as well </li>
	<li> After you start the script, you have to wait depending on how many books you have provided. You can also provide as a parameter how many words you want to extract from each word </li>
	<li> After the extraction is ready, the generated file will be "/tmp/ops.json" </li>
</ul>

classify.py
<ul>
	<li> You must call the script with 2 parameters - *path to the dataset* and *path to the book* </li>
	<li> The scipt will return an F1 score of the training and a predicted genre of the books <li>
</ul>
