def count_digits(card_number):
	if card_number/10 != 0:
		digits = card_number%10
		digits = card_number/10
	return digits


print count_digits(1234567891234567)