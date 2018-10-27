def encode(phrase):
	phraseList = phrase.split()
	vowels = ("aeiouy")
	for x in range (len(phraseList)):
		if phraseList[x][0] in vowels:
			phraseList[x] = phraseList[x] + "yay"
		else:
			for y in range(len(phraseList[x])):
				if phraseList[x][y] in vowels:
					phraseList[x] = phraseList[x][y:] + phraseList [x][:y] + "ay"
					break
		return (" ".join(phraseList)).lower()