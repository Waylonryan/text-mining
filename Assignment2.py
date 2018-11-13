from imdbpie import Imdb
from collections import Counter
from nltk import FreqDist

imdb = Imdb()
print(imdb.search_for_title("Inception")[0])
reviews = imdb.get_title_user_reviews("tt1375666")


blackbook = [reviews['reviews'][0]['reviewText']]
blackbook.append(reviews['reviews'][1]['reviewText'])
blackbook.append(reviews['reviews'][2]['reviewText'])
blackbook.append(reviews['reviews'][3]['reviewText'])
blackbook.append(reviews['reviews'][4]['reviewText'])
blackbook.append(reviews['reviews'][5]['reviewText'])
blackbook.append(reviews['reviews'][6]['reviewText'])
blackbook.append(reviews['reviews'][7]['reviewText'])
blackbook.append(reviews['reviews'][8]['reviewText'])
blackbook.append(reviews['reviews'][9]['reviewText'])
blackbook.append(reviews['reviews'][10]['reviewText'])
blackbook.append(reviews['reviews'][11]['reviewText'])
blackbook.append(reviews['reviews'][12]['reviewText'])
blackbook.append(reviews['reviews'][13]['reviewText'])
blackbook.append(reviews['reviews'][14]['reviewText'])
blackbook.append(reviews['reviews'][15]['reviewText'])
blackbook.append(reviews['reviews'][16]['reviewText'])
blackbook.append(reviews['reviews'][17]['reviewText'])
blackbook.append(reviews['reviews'][18]['reviewText'])
blackbook.append(reviews['reviews'][19]['reviewText'])
blackbook.append(reviews['reviews'][20]['reviewText'])
blackbook.append(reviews['reviews'][21]['reviewText'])
blackbook.append(reviews['reviews'][22]['reviewText'])
blackbook.append(reviews['reviews'][23]['reviewText'])
blackbook.append(reviews['reviews'][24]['reviewText'])


f = open("blackbook.txt", "w")
new = [blackbook]
f.write("\n".join(map(lambda x: str(x), new)))
f.close()
