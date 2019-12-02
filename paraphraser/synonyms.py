# for tagger importing
import pickle
f = open('tagger.pickle','rb')
tagger = pickle.load(f)
f.close()



from nltk.corpus import wordnet
# for sentence tokenizer, it's more efficient
import nltk.data as nldat
sen_token = nldat.load('tokenizers/punkt/PY3/english.pickle')
from nltk.tokenize import word_tokenize
import random

random.seed()



'''
replace_with_syn is the function of target
'''
def replace_with_syn(inp):
	sentences = sen_token.tokenize(inp)
	resen=[]
	for i in sentences:
		resen.append(with_syn(i))
	resen=" ".join(resen)
	return resen

def with_syn(sentence):
	words = word_tokenize(sentence)
	tagged = tagger.tag(words)
	alter=[]
	for i in range( len(tagged) ):
		if tagged[i][1][0]=='N':
			alter.append(find_synn(tagged[i][0]))
		elif tagged[i][1][0]=='J':
			alter.append(find_synj(tagged[i][0]))
		else:
			alter.append(tagged[i][0])
	alter = " ".join(alter)
	return alter

def find_synn(word):
	try:
		syn = wordnet.synsets(word,pos='n')
		sim = 0
		replacing=False
		while sim<0.5 or len(syn)>0:
			temp = random.choice(syn)
			ts = wordnet.synset(temp.name())
			sim = wordnet.synset(word+'.n.01').wup_similarity(ts)
			if word==(temp.lemmas())[0].name():
				syn.remove(temp)
			elif sim>=0.5:
				replacing=True
				syn=temp
				break
			else:
				syn.remove(temp)
		if replacing==True:	
			lem=syn.lemmas()
			return lem[0].name()
		else:
			return word
	except:
		return word

def find_synj(word):
	try:
		syn = wordnet.synsets(word,pos='a')
		sim = 0
		replacing=False
		while sim<0.4 or len(syn)>0:
			temp = random.choice(syn)
			ts = wordnet.synset(temp.name())
			sim = wordnet.synset(word+'.a.01').wup_similarity(ts)
			if word==(temp.lemmas())[0].name():
				syn.remove(temp)
			elif sim>=0.4:
				replacing=True
				syn=temp
				break
			else:
				syn.remove(temp)
		if replacing==True:	
			lem=syn.lemmas()
			return lem[0].name()
		else:
			return word
	except:
		return word

