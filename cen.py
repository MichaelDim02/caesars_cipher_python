# Python implementation of the Caesar cipher (encryption script) #
# MCD 2020 GPLv3 #
import sys

alphabet_doubled = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encrypt():
	en_text = ""
	for character in plain_text:
		count = 0
		for alph_char in alphabet_doubled[:26]:
			count = count + 1
			if alph_char == character:
				en_text = en_text+ alphabet_doubled[count+value]
				break
			elif count >= 26:
				en_text = en_text + character

	print(en_text)

if( len(sys.argv) > 2 ):
	value = int(sys.argv[1]) - 1
	plain_text = sys.argv[2].lower()
	try:
		encrypt()
	except:
		print("\nTerminated.")
else:
	print("Usage: python cen.py [VALUE] [PLAIN_TEXT]")
	print("Example: python cen.py 4 \'hello\'")
	exit(0)
