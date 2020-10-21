# Python implementation of the Caesar cipher (decryption script)#
# MCD 2020 #
import sys

alphabet_doubled = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def decrypt():
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
	
	print(de_text)

if( len(sys.argv) > 2 ):
	value = - (int(sys.argv[1]) + 1)
	en_text = sys.argv[2].lower()
	try:
		decrypt()
	except:
	        print("Terminated.")
else:
	print("Usage: python cde.py [VALUE] [EN_TEXT]")
	print("Example: python cde.py 4 \'lipps\'")
	exit(0)
