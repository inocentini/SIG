import os
from operator import itemgetter


file = open("ciphertext_analise_frequencia.txt") 
cnt = 0
letter = []
while True:
	char = file.read(1)
	cnt += 1
	if not char: break
	if char is not "" and char is not ',' and char is not '.' and char is not ':' and char is not '(' and char is not ')': letter.append(char)

size = len(letter)
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
dict ={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
for i in range(size):
	if letter[i] == 'A':
		dict['A'] += 1/size * 100
	if letter[i] == 'B':
                dict['B'] += 1/size * 100
	if letter[i] == 'C':
                dict['C'] += 1/size * 100
	if letter[i] == 'D':
                dict['D'] += 1/size * 100
	if letter[i] == 'E':
                dict['E'] += 1/size * 100
	if letter[i] == 'F':
                dict['F'] += 1/size * 100
	if letter[i] == 'G':
                dict['G'] += 1/size * 100
	if letter[i] == 'H':
                dict['H'] += 1/size * 100
	if letter[i] == 'I':
                dict['I'] += 1/size * 100
	if letter[i] == 'J':
                dict['J'] += 1/size * 100
	if letter[i] == 'K':
                dict['K'] += 1/size * 100
	if letter[i] == 'L':
                dict['L'] += 1/size * 100
	if letter[i] == 'M':
                dict['M'] += 1/size * 100
	if letter[i] == 'N':
                dict['N'] += 1/size * 100
	if letter[i] == 'O':
                dict['O'] += 1/size * 100
	if letter[i] == 'P':
                dict['P'] += 1/size * 100
	if letter[i] == 'Q':
                dict['Q'] += 1/size * 100
	if letter[i] == 'R':
                dict['R'] += 1/size * 100
	if letter[i] == 'S':
                dict['S'] += 1/size * 100
	if letter[i] == 'T':
                dict['T'] += 1/size * 100
	if letter[i] == 'U':
                dict['U'] += 1/size * 100
	if letter[i] == 'V':
                dict['V'] += 1/size * 100
	if letter[i] == 'W':
                dict['W'] += 1/size * 100
	if letter[i] == 'X':
                dict['X'] += 1/size * 100
	if letter[i] == 'Y':
                dict['Y'] += 1/size * 100
	if letter[i] == 'Z':
                dict['Z'] += 1/size * 100

desc = []
for item in dict:
	temp = {
		"letter": item,
		"freq": dict.get(item)
		}
	desc.append(temp)

newList = sorted(desc, key=itemgetter('freq'), reverse=True)
print("Analise das frequencias e ordenação decrescente:")
for tupla in newList:
	print(tupla)

tabelaDeco = []

for item, i in zip(dict,range(26)):
	if (i+11 < len(newList)):
		tabelaTemp = {
				"plaintext":item,
				"cipher":alpha[i+11]
			}
	else:
		tabelaTemp = {
				"plaintext": item,
				"cipher": alpha[i-15]
			}
	tabelaDeco.append(tabelaTemp)

print("Tabelação do plaintext com o ciphertext")
for dupla in tabelaDeco:
	print(dupla)
text = ""
print("Descriptografica")
for i in range(size):
	for j in range(26):
		if(letter[i] == tabelaDeco[j]['cipher']):
			text = text + tabelaDeco[j]['plaintext']
			break

print(text)
