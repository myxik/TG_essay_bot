import tensorflow as tf
from embeddings import load_sentence_embeddings
from preprocess_data import preprocess_batch
from six.moves import input
from lstm_model import lstm_model
import numpy as np
from pprint import pprint as pp
from inference import Paraphraser


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
				if p_sentence.lower().split(' ').remove('.')==sentence.lower().split(' '):
					continue
				else:
					return p_sentence
			except ValueError:
				if p_sentence.lower().split(' ')==sentence.lower().split(' '):
					continue
				else:
					return p_sentence


inpt = input()
print(paraphrase(inpt))