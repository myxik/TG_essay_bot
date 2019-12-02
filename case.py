import pickle
f = open('tagger.pickle','rb')
tagger = pickle.load(f)
f.close()

import nltk.data as nldat
sen_token = nldat.load('tokenizers/punkt/PY3/english.pickle')
from nltk.tokenize import word_tokenize


def case_change(inp):
	sentences = sen_token.tokenize(inp.lower())
	resen = []
	for i in sentences:
		resen.append(proper_casing(i))
	resen1 = " ".join(resen)
	return resen1


def proper_casing(sent):
	words = word_tokenize(sent)
	words[0]=words[0].title()
	tagged = tagger.tag(words)
	alter=[]
	for i in range( len(tagged) ):
		if tagged[i][1]=='NNP': #or 'NNPS'
			alter.append( tagged[i][0].title() )
		elif tagged[i][1]=='NNPS':
			alter.append( tagged[i][0].title() )
		else:
			alter.append( tagged[i][0] )
	alters = ' '.join(alter[:-1])
	alters += alter[-1]
	return alters



