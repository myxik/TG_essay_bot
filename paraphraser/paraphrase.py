import tensorflow as tf
from embeddings import load_sentence_embeddings
from preprocess_data import preprocess_batch
from six.moves import input
from lstm_model import lstm_model
import numpy as np
from pprint import pprint as pp
from inference import Paraphraser
from synonyms import replace_with_syn

def paraphrase(sentence):
	"""Outputs a paraphrased sentence str. 
	Args:
		sentence: str
	"""
	p = Paraphraser('model-171856')
	for i in range(10):
		paraphrases = p.sample_paraphrase(sentence, sampling_temp=0.1*(i+1), how_many=100)
		for j, p_sentence in enumerate(paraphrases):
			try:
				repl = replace_with_syn(p_sentence)
				if repl.lower().split(' ').remove('.')==sentence.lower().split(' '):
					continue
				else:
					tripl_p = p.sample_paraphrase(repl, sampling_temp=0.1, how_many=1)
					return repl if tripl_p.lower().split(' ').remove('.')==sentence.lower().split(' ') else tripl_p
			except ValueError:
				repl = replace_with_syn(p_sentence)
				if repl.lower().split(' ')==sentence.lower().split(' '):
					continue
				else:
					tripl_p = p.sample_paraphrase(repl, sampling_temp=0.1, how_many=1)
					return repl if tripl_p.lower().split(' ')==sentence.lower().split(' ') else tripl_p