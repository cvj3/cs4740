from common import END_SENTENCE_PUNCT, add_word_to_sentence, weighted_random_pick
import random

def build_bigram_model(tokens):
	bigram_model = {}
	for i in range(len(tokens) - 1):
		token_curr = tokens[i]
		token_next = tokens[i + 1]
		bigram_model[token_curr] = bigram_model.get(token_curr, {})
		bigram_model[token_curr][token_next] = bigram_model[token_curr].get(token_next, 0) + 1
	return bigram_model

def write_bigram_to_file(bigram_model, name):
	f = open("saved_models/" + name + ".py", "w")
	str_model = str(bigram_model).replace(", ", ",\n\t").replace("{","{\n\t").replace("}","\n}").replace("},\n\t", "},\n").replace("\t","",1)
	write_str = 'model = ' + str_model
	f.write(write_str)
	f.close()

def word_from_bigram_model_and_previous_word(bigram, word):
	word = weighted_random_pick(bigram[word])
	return word

def generate_bigram_sentences(bigram_model, number, sentence="", starting_word="."):
	for i in range(number):
		if starting_word != "." and not bigram_model.get(starting_word):
			starting_word = "."
			sentence = ""
			print "Error occured, starting word '" + starting_word + "' "
		while starting_word in END_SENTENCE_PUNCT:
			starting_word = random.choice(bigram_model.keys())
		if not sentence: sentence = starting_word.title()
		base_word = starting_word
		word = None
		while word not in END_SENTENCE_PUNCT:
			word = word_from_bigram_model_and_previous_word(bigram_model, base_word)
			sentence, word = add_word_to_sentence(sentence, word)
			if word:
				base_word = word
		try:
			print sentence
		except:
			print "Could not print sentence due to an unrecognized character."
		print "\n"
