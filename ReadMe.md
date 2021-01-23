Guidance: <a href="https://www.linkedin.com/in/boris-velichkov-298b0a66/"> Boris Velichkov, FMI </a> </br>
Sources:
<ul>
	<li> noise_data:
		<ul>
			<li> <a href="https://datahub.io/core/world-cities#data">city_names</a> </li>
			<li> <a href="https://bg.wikipedia.org/wiki/%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BB:%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D0%B5_%D0%B2_%D1%81%D0%B2%D0%B5%D1%82%D0%B0">country_names</a> </li>
			<li> <a href="http://www.nrscotland.gov.uk/files/statistics/pop-names-07-t4.csv">human_names</a></li>
			<li> <a href="https://github.com/stopwords-iso/stopwords-bg"> stopwords </a> </li> 
		</ul>
	</li>
	<li> Libraries:
		<ul>
			<li> <a href="https://pypi.org/project/bulstem/"> bulstem </a> </li>
			<li> <a href="https://scikit-learn.org/stable/"> sklearn <a> </li>
		</ul>
	</li>
	<li> Articles:
		<ul>
			<li> <a href="https://www.analyticsvidhya.com/blog/2019/04/predicting-movie-genres-nlp-multi-label-classification/"> Main ML idea </a> </li>
			<li> <a href="https://towardsdatascience.com/journey-to-the-center-of-multi-label-classification-384c40229bff"> Multi-label classification idea </a> </li>
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
	<li> The scipt will return an F1 score of the training and a predicted genre of the books </li>
</ul>

Tests explained:
<ul>
	<li> Test 0
		The idea was to pick the top 3 datasets that I had based on an F1 score. Since a single test on a single dataset was ~10 hours, I had to do it only on some of the datasets </li>
	<li> Test 1
		<ul>
			<li> features: 2,000 - 20,000 </li>
			<li> data_split: 0.1 - 0.45 </li>
			<li> threshold: 0.1 - 0.45 </li>
			<li> №tests: 20 </li>
		</ul>
		Results showed that the best solution has to be in this range:
		<ul> 
			<li> features: 5,000 - 14000 </li>
			<li> data_split: 0.1 - 0.25 </li>
			<li> threshold: 0.25 - 0.3 </li>
		</ul>
	</li>
	<li> Test 2
        <ul>
            <li> features: 5,000 - 14,000 </li>
            <li> data_split: 0.1 - 0.25 </li>
            <li> threshold: 0.25 - 0.3 </li>
            <li> №tests: 25 </li>
        </ul>
        Results showed that the best solution has to be in this range:
        <ul>
            <li> features: 5,000 - 10000 </li>
            <li> data_split: 0.1 - 0.15 </li>
            <li> threshold: 0.25 - 0.3 </li>
        </ul>
    </li>
    <li> Test 3
        <ul>
            <li> features: 5,000 - 10,000 </li>
            <li> data_split: 0.1 - 0.15 </li>
            <li> threshold: 0.25 - 0.3 </li>
            <li> №tests: 35 </li>
        </ul>
        Results showed that the best solution has to be in this range:
        <ul>
            <li> features: 7,000 </li>
            <li> data_split: 0.1 </li>
            <li> threshold: 0.26 </li>
        </ul>
    </li>
    <li> Test 4
        <ul>
            <li> features: 7,000 </li>
            <li> data_split: 0.1 </li>
            <li> threshold: 0.26 </li>
            <li> № tests: 50 </li>
		</ul>
		Results showed that the best possible solution in terms of F1 score is for the 1125 words dataset and it is 0.8759894459102902 </br>
		Note that it is overfitting and this is not the most optimal solution of the task.
	</li>
</ul>
