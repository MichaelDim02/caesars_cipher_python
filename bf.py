import sys
import collections
from collections import Counter

#token_freq = ["e","t","o","a","i","n","s","h","r","l","u","d","y","m","w","g","f","c","b","p","k","v","j","x","z","q"]

#n_t_freq = [5,20,15,1,9,14,19,8,18,12,21,4,25,13,23,7,6,3,2,16,11,22,10,24,26,17]

words = [' i ',' a ', 'about ', 'all ', 'also ', 'and ', ' as ', 'at ', ' be ', 'because ', 'but ', 'by ', 'can ', 'come ', 'could ', 'day ', ' do ', 'even ', 'find ', 'first ', 'for ', 'from ', 'get ', 'give ', 'go ', 'have ', 'he ', 'her ', 'here ', 'him ', ' his ', ' how ', ' if ', 'in ', 'into ', ' it ', ' its ', 'just ', 'know ', 'like ', 'look ', 'make ', 'man ', 'many ', 'me ', 'more ', 'my ', 'new ', ' no ', ' not ', 'now ', ' of ', ' on ', 'one ', 'only ', ' or ', 'other ', ' our ', ' out ', 'people ', ' say ', ' see ', 'she ', ' so ', 'some ', 'take ', 'tell ', 'than ', 'that ', 'the ', 'their ', 'them ', 'then ', 'there ', 'these ', 'they ', 'thing ', 'think ', 'this ', 'those ', 'time ', ' to ', 'two ', ' up ', ' use ', 'very ', 'want ', ' way ', ' we ', 'well ', 'what ', 'when ', 'which ', 'who ', 'will ', 'with ', 'would ', 'year ', 'you ', 'your ']

alphabet_doubled = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def crack():
	for value in range(1,27):
		value = -(value + 1)
		de_text = ""
		for character in en_text:
			count = 0
			for alph_car in alphabet_doubled[:26]:
				count = count + 1
				if alph_car == character:
					de_text = de_text + alphabet_doubled[count+value+26]
					break
				elif count >= 26:
					de_text = de_text + character
		if any(word in de_text for word in words):
			print("\n",-value-1,":",de_text,"\n")
		else:
			print(-value-1,":",de_text)

if(len(sys.argv) >1):
	en_text = sys.argv[1].lower()
	counts=Counter(en_text) 
	try:
		crack()
	except:
		print("Terminated.")
else:
	print("Usage: python bf.py [EN_TEXT]")
	print("Example: python bf.py 'lipps'")
	exit(0)
