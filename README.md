**Automatically tagged 20th century Spanish poems from The Diachronic Spanish Sonnet Corpus (DISCO, Ruiz Fabo et al. 2017)**

In this project we have taken the 20th century sonnets located in DISCO and wrote simple code to automatically tag them for four phonetic features of interest to those learning and teaching L2 Spanish phonetics. It is our hope that a Spanish phonetics instructor who wishes to find authentic materials for pronunciation practice and/or IPA-transcription exercises could use this dataset to save time in lesson planning. Below is an explanation of each of the columns in this dataset:

•	**file**:		The individual poem’s filename 
•	**text**:		The individual poem text
•	**title**:		The individual poem title
•	**author**: 	The author of the poem
•	**author_id**:	The author ID marker as taken from DISCO
•	**place-birth**:	The author’s place of birth
•	**country-birth**:	The author’s country of birth
•	**gender**:		The author’s gender

Each of the above entries were taken directly from DISCO. As the dataset shows, there is a good mix of poems from a diverse array of authors. Our novel additions consist of the columns below:

•	**vowellink**: We tagged all instances where a word ends with a vowel, and the following word begins with the same vowel, for those who wish to practice synalepha (the linking of two vowels into one). 
•	**stop**: We tagged instances in which the stop consonants [bdg] would occur, which we tagged as after a pause or after a nasal consonant /n/ or /m/. We find that the stop allophones are less frequent than their approximant counterparts- thus, we thought it would be more useful to tag the stops, and to thus give an idea of which poems would have a better balance of stops and approximants.
•	**trill**: We tagged instances in which the alveolar trill [r] would appear: at orthographic double r and in word-initial position. After the nasal consonant [n] was also tagged.
•	**sonorization**: We tagged instances in which /s/ would be pronounced as [z]: whenever orthographic s or z appears before a voiced consonant.

For each of the four columns above, you will find a copy of the poem text, with the tag in question appearing in between brackets [ ]. We have also included simple counts of these tags in the following columns:

•	**vowellink_count**: A simple count of the number of vowellink tags that occur in the poem
•	**stop_count**: A simple count of the number of stop tags that occur in the poem
•	**trill_count**: A simple count of the number of trill tags that occur in the poem
•	**sonorization_count**: A simple count of the number of sonorization tags that occur in the poem
•	**tag_sum**: The sum of the vowellink_count, stop_count, trill_count, and sonorization_count tags

The code for the automatic tagging process can be found in sonnets.py. We hope you find this dataset useful in your Spanish language learning and teaching. 

Bibliography

Ruiz Fabo, Pablo, Helena Bermúdez Sabel, Clara Martínez Cantón, and José Calvo Tello. 2017. Diachronic Spanish Sonnet Corpus (DISCO). Madrid: UNED. https://github.com/pruizf/disco. 
![image](https://github.com/coltonsea/SPLAT/assets/125835820/8c04bad1-dcec-40c2-a354-fd1fbc607c16)
