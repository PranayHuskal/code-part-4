#5. Accept on character from user and check whether that character is vowel (a,e,i,o,u) or not.
def chkvowel(ch):
	if (ch.lower()) in ('a','e','i','o','u'):
		print('True',ch,'is vowel')
	else:
		print('False',ch,'is not vowel')



a=(input("enter a character: "))
chkvowel(a)