def replace_letter(original_letter, replacement_letter, word):
	new_word = ""

	for i in range(0, len(word)):
		if word[i] == original_letter:
			new_word += replacement_letter
		else:
			new_word += word[i]
	return new_word

def switch_letters(original_letter, replacement_letter, word):
	new_word = ""

	for i in range(0, len(word)):
		if word[i] == original_letter:
			new_word += replacement_letter
		elif word[i] == replacement_letter:
			new_word += original_letter
		else:
			new_word += word[i]
	return new_word

def switch_words(first_word, second_word, sentence):
	new_sentence = ""
	new_word = ""

	for i in range(0, len(sentence)):
		if sentence[i] == " ":
			new_sentence += (new_word + " ")
			new_word = ""
		else:
			new_word += sentence[i]
			if new_word == first_word:
				new_word = ""
				new_sentence += second_word
			elif new_word == second_word:
				new_word = ""
				new_sentence += first_word
	return new_sentence

def censor_text(sentence):
	innapropriate_list = ["crappy", "dumb", "stupid"]
	replacement_list = ["######", "@@@@", "******"]
	new_sentence = ""
	new_word = ""
	for i in range(0, len(sentence)):
			if sentence[i] == " ":
				new_sentence += (new_word + " ")
				new_word = ""
			else:
				new_word += sentence[i]
				for j in range(0, len(innapropriate_list)):
					if new_word == innapropriate_list[j]:
						new_word = ""
						new_sentence += replacement_list[j]
	return new_sentence


print replace_letter("a", "l", "banana")
print switch_letters("e", "o", "textbook")
print switch_words("fox", "dog", "The quick brown fox jumps over the lazy dog") 
print censor_text("The dumb brown fox jumps over the stupid, crappy, lazy dog. Isn't that so dumb?")