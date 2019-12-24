
import os
from utils import is_file,ls
from news import NewsCorpus
from arabic import unicodeArabic,lettersWaits
import random 


def score(article,method="average",average_article_length=1):
	score = 0
	letters_count = 0
	for u_letter in article:
		if u_letter in unicodeArabic:
			letter = unicodeArabic[u_letter]
			if letter in lettersWaits:
				score += lettersWaits[letter]
			letters_count += 1
	if letters_count <= 0:
		return 0
	
	if method == "average":
		return score/letters_count
	elif method == "sum":
		return score
	elif method == "global_average":
		return score/average_article_length



def get_param():
	"""
	handle command line parameters, test using -h parameter....
	"""
	import argparse
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('-d','--dataset',help='dataset path (file or directory)',default=None)
	parser.add_argument('-m','--method',help='scoring method (average, sum, global_average)',default="sum")
	parser.add_argument('-n','--minlen',help='article minimum length',default=50)
	parser.add_argument('-x','--maxlen',help='article maximum length',default=500)
	

	args = parser.parse_args()
	

	return args.dataset,args.method,args.minlen,args.maxlen

def main():

	dataset,method,minlen,maxlen = get_param()	
	corpus = NewsCorpus(0,"News",dataset)
	global_average = 1
	if method == "global_average":
		global_average = sum([len(a.clean_content) for a in corpus])/len(corpus)

	scores = []
	for article in corpus:
		text = article.clean_content
		if len(text) < minlen:
			scores.append(0)
			continue
		if len(text) > maxlen:
			text = random.sample(text,maxlen)
		scores.append(score(text,method,global_average))
	import operator
	index, value = max(enumerate(scores), key=operator.itemgetter(1))

	print(f"Best Article Score: {value}")
	print()
	print(corpus[index])



if __name__ == '__main__':
	main()