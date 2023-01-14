
words = ['ADJECTIVE', 'VERB', 'NOUN', 'NOUN']
with open('sentence1.txt') as sentence:
    sentence = sentence.read()

for i in words:
    while i in sentence:
     new_word = input("Enter an " + i + ": " )
     sentence = sentence.replace(i, new_word,1)

print(sentence)

with open("new_sentence.txt", 'w') as sentence2:
	sentence2.write(sentence) 
