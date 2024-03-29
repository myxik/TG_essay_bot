import tensorflow as tf
from embeddings import load_sentence_embeddings
from preprocess_data import preprocess_batch
from six.moves import input
from lstm_model import lstm_model
import numpy as np
from pprint import pprint as pp
from inference import Paraphraser
from synonyms import replace_with_syn, sentence_separator

def paraphrase(sentence):
	"""Outputs a paraphrased sentence str. 
	Args:
		sentence: str
	"""
	p = Paraphraser('model-171856')
	for k in sentence_separator(sentence):
		for i in range(5):
			paraphrases = p.sample_paraphrase(k, sampling_temp=0.1*(i+1), how_many=5)
			for j, p_sentence in enumerate(paraphrases):
				try:
					repl = replace_with_syn(p_sentence)
					prob1 = repl
					if prob1.lower().split(' ').remove('.')==k.lower().split(' '):
						continue
					else:
						tripl_p = p.sample_paraphrase(repl, sampling_temp=0.1, how_many=1)
						return ' '.join(repl) if tripl_p.remove('.')==k else ' '.join(tripl_p)
				except ValueError:
					prob2 = repl
					if prob2.lower().split(' ')==k.lower().split(' '):
						continue
					else:
						tripl_p = p.sample_paraphrase(repl, sampling_temp=0.1, how_many=1)
						return ' '.join(repl) if tripl_p==k else ' '.join(tripl_p)
