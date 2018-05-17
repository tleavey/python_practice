# My Code to make the Markov chain work

import sys
from markovEngine import *

def create_model(filename):
	infile = open(filename)
	model = Markov()
	for line in infile:
		words = line.split()
		for word in words:
			model.add(word)
	infile.close()
	model.add(None)
	model.reset()
	return model

def generate_word_chain(markov, n):
	words = []
	for i in range(n):
		next_word = markov.next_word()
		if next_word is None: break 
		words.append(next_word)
	return " ".join(words)

filename = sys.argv[1]
markov = create_model(filename)
words = generate_word_chain(markov, 1000)
print words