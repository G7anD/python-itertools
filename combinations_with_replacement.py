# itertools noname function examples by GranD_MasTeR
import itertools as it
letter = ['a', 'b', 'c', 'd', 'e']
numbers = [0, 1, 2, 3, 4]
twrd = ['hi', 'bye']

k = list(it.combinations(it.chain(letter, numbers, twrd),3))

for i in k:
	print(i,end=" *** ")