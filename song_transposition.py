lyrics = """
        C                G                D      
When I saw you in that dress, looking so beautiful
  Em       C                  G        D            G 
I don't deserve this, darling you look perfect tonight
"""

flat_chords = ['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab']
sharp_chords=['A','A#','B','C','C#','D','D#','E','F','F#','G', 'G#']

def transpose(half_step):
	new_lyrics = ""
	new_word = ""

	for i in range (0, len(lyrics)):
		if lyrics[i] == " ":
			new_lyrics += (new_word + " ")
			new_word = ""
		else:
			new_word += lyrics[i]
			
			if 'Bb' or 'Db' or 'Eb' or 'Gb' or 'Ab' in lyrics:
				for j in range(0, len(flat_chords)):				
					if new_word == flat_chords[j]:
						new_word = ""
						new_lyrics += flat_chords[j + half_step]
						if 0 > j:
							j = len(flat_chords) - 1
						elif j > len(flat_chords) - 1:
							j = 0
			if 'A#' or 'C#' or 'D#' or 'F#' or 'G#' in lyrics:
				for j in range(0, len(sharp_chords)):				
					if new_word == sharp_chords[j]:
						new_word = ""
						new_lyrics += sharp_chords[j + half_step]

	new_lyrics += (new_word + " ")

	return new_lyrics



print lyrics
print transpose(-5)