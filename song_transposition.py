lyrics = """
        C                G                D      
When I saw you in that dress, looking so beautiful
  Em       C                  G        D            G 
I don't deserve this, darling you look perfect tonight
"""


standard_chords = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
flat_chords = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
sharp_chords = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
other_chords =  ['min', 'm', 'min7', '3', '7', 'maj7', 'm7', 'major7', 'sus2', 'sus4', 'add9', 'minadd9', 'add6', 'minadd6']

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

			elif 'A#' or 'C#' or 'D#' or 'F#' or 'G#' in lyrics:
				for j in range(0, len(sharp_chords)):				
					if new_word == sharp_chords[j]:
						new_word = ""
						new_lyrics += sharp_chords[j + half_step]
						if 0 > j:
							j = len(sharp_chords) - 1
						elif j > len(sharp_chords) - 1:
							j = 0

			else:
				for j in range(0, len(standard_chords)):
					if new_word == standard_chords[j]:
						if new_word == standard_chords[j] + 'min' or 'm' or 'min7' or '3' or '7' or 'maj7' or 'm7' or 'major7' or 'sus2' or 'sus4' or 'add9' or 'minadd9' or 'add6' or 'minadd6':
							new_word = ""
						new_lyrics += standard_chords[j + half_step]
						if 0 > j:
							j = len(standard_chords) - 1
						elif j > len(standard_chords) - 1:
							j = 0

	new_lyrics += (new_word + " ")

	return new_lyrics



print lyrics
print transpose(-5)