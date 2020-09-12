

def anagrams(word, words):
	#your code here
	from collections import Counter

	word1=Counter(word)
	word1=sorted(word1.items())

	words1=[Counter(i) for i in words]
	words1 = [sorted(i.items()) for i in words1]
	
	resultado = [words[i] for i in range(len(words1)) if word1 == words1[i]]
	
	print(resultado)

	
    	


anagrams('laser', ['lazing', 'lazy',  'lacer'])

#def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]