import random

field_start = 1
field_cur = field_start
fields_special = {
	4: 16,	#ladder
	12: 33,	#ladder
	18: 22,	#ladder
	21: 3,	#snake
	24: 7,	#snake
	26: 37,	#ladder
	35: 9,	#snake
	42: 61,	#ladder
	49: 51,	#ladder
	50: 11,	#snake
	53: 15,	#snake
	55: 74,	#ladder
	60: 23,	#snake
	75: 44,	#snake
	82: 98,	#ladder
	85: 95,	#ladder
	88: 92,	#ladder
	89: 48,	#snake
	93: 25,	#snake
	97: 65,	#snake
	99: 58	#snake
	}
solves = 0
rolls_solved = 0
avrg = 0.0
solves_max = 100000000 #100.000.000
rolls_cur = 0
random.seed()
shortest = 100000
longest = 0

print(f"solves: {solves} - rolls_solved: {rolls_solved} - avrg: {avrg}", end='')

while solves < solves_max:
	dice = random.randrange(6) + 1 #random.randrange(6) = 0,1,2,3,4,5
	rolls_cur += 1
	field_cur += dice
	if field_cur in fields_special:
		field_cur = fields_special[field_cur]

	if field_cur >= 100:
		solves += 1
		rolls_solved += rolls_cur
		avrg = rolls_solved/solves
		if rolls_cur > longest:
			longest = rolls_cur
		elif rolls_cur < shortest:
			shortest = rolls_cur
		print(f"\rsolves: {solves} - rolls_solved: {rolls_solved} - avrg: {avrg:.4f} - shortest: {shortest} - longest: {longest}", end='')
		rolls_cur = 0
		field_cur = field_start