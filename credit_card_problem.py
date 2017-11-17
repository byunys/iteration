def count_digits(card_number):
	digits = 0
	end_digit = 0
	if card_number/10 != 0:
		card_number/10
		digits += 1
	else:
		end_digit = 1
	return digits + end_digit


print count_digits(5424180123456789)