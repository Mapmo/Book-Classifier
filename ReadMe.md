<h3>Guidance: <a href="https://www.linkedin.com/in/boris-velichkov-298b0a66/"> Boris Velichkov, FMI </a> </h3>
<h3>Sources:</h3>
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

<h3>How the project works:</h3>
<ul>
	<li> extract.py - generates a dataset in JSON format from the most common words in each book </li>
	<li> classify.py - using a specified dataset, created by extract.py, it classifies the genre(s) of a book after learning on the provided dataset </li>
    <li> reqs.txt - contains all the requirements needed for the scripts, can be used from pip </li>


  ```bash
   $ pip install -r reqs.txt
  ```

</ul>

<h3>Usage:</h3>
<b>extract.py</b>
<ul>
	<li> You must be located in a directory that contains other directories named after their genres </li>
	<li> The script will be looking for a txt directory for each genre. This is useful in case you want to have zip files for the books in each genre as well </li>
	<li> After you start the script, you have to wait depending on how many books you have provided. You can also provide as a parameter how many words you want to extract from each word </li>
	<li> After the extraction is ready, the generated file will be "/tmp/ops.json" </li>

```bash
$ ls
Ancient  Classics  Criminal  Fantasy  Horror  Humour  Love  Science  Sci-Fi  Social
$ ls Ancient/
all_links  Ancient.words  txt  zips
$ ls Ancient/txt/ | head
110-Herodot_-_Istoricheski_noveli.txt
141-William-Shakespeare_-_Soneti.txt
1492-Nikolaj_Kun_-_Starogrytski_legendi_i_mitove.txt
1642-Jean-Froissart_-_Hroniki.txt
1696-Sun_Dzy_-_Izkustvoto_na_vojnata.txt
1840-Jean-Pierre-Vernant_-_Starogrytski_mitove_-_Vsemiryt_bogovete_horata.txt
1984-Konfutsij_-_Dobrijat_pyt_-_Misli_na_velikija_kitajski_mydrets.txt
2074-Genro_-_Zheljaznata_flejta_sto_dzenski_koana_-_Slovata_na_dzenskite_mydretsi.txt
217-Starogrytska_lirika.txt
29-Giovanni-Boccaccio_-_Dekameron.txt
$ ~/Git/Book-Classifier/extract.py
Starting Ancient
Starting Classics
Starting Criminal
Starting Fantasy
Starting Horror
Starting Humour
Starting Love
Starting Science
Starting Sci-Fi
Starting Social
```

</ul>

<b>classify.py</b>
<ul>
	<li> You must call the script with 2 parameters - *path to the dataset* and *path to the book* </li>
	<li> The scipt will return an F1 score of the training and a predicted genre of the books </li>

```bash
$ ./classify.py /tmp/ops.json Omir_-_Iliada_-_6122-b.txt
/usr/local/lib/python3.6/site-packages/pandas/compat/__init__.py:120: UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.
  warnings.warn(msg)
0.6937984496124031
[('Ancient',)]

```
</ul>

<h3>Tests explained:</h3>
<ul>
	<li> Test 0
		The idea was to pick the top 3 datasets that I had based on an F1 score. Since a single test on a single dataset was ~10 hours, I had to do it only on some of the datasets </li>
	<li> Test 1
		<ul>
			<li> features: 2,000 - 20,000 </li>
			<li> data_split: 0.1 - 0.45 </li>
			<li> threshold: 0.1 - 0.45 </li>
			<li> № tests: 20 </li>
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
            <li> № tests: 25 </li>
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
            <li> № tests: 35 </li>
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
	<li>
		Tests with books that were not part of the training process
		<ul>
			<li> Test Hannibal
				<ul>
					<li> Tests with 0.15 thresholds were accurate and tests with more than 1000 top words and threshold 0.125 were accurate as well</li>
				</ul>
			</li>
			<li> Test Twilight
				<ul>
					<li> Tests with threshold over 0.1 were accurate</li>
				</ul>
			</li>
			<li> Test Game of Thrones
				<ul>
					<li> Tests with threshold 0.1 and above were accurate</li>
				</ul>
			</li>
			<li> Test Naked Sun
				<ul>
					<li> Tests with 0.1 threshold and above and	over 950 words were accurate</li>
				</ul>
			</li>
			<li> Test Azazel
				<ul>
					<li> Tests with 0.125 threshold and top words between 1000 and 1250 were accurate</li>
				</ul>
			</li>
		</ul><br>
		As a result from the tests, especially that from Azazel, datasets with top 1125 an 1250 top words seem the most accurate. and since the F1 score of 1250 is a bit higher, this is the dataset that I consider a winner
	</li>
</ul>
