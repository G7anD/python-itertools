# itertools compress function examples by GranD_MasTeR
import itertools as it

letter = ['a', 'b', 'c', 'd', 'e']
numbers = [0, 1, 2, 3, 4]
tek = [True, False, True, False, True]

f = list(it.compress(letter, tek))
f2 = list(it.compress(numbers, tek))

print(f, f2, sep="\n")
