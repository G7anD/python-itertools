# itertools combinations function examples by GranD_MasTeR
import itertools as it

letter = ['a', 'b', 'c', 'd', 'e']
numbers = [0, 1, 2, 3, 4]
twrd = ['hi', 'bye']

k = it.combinations(letter, 4)
for i in k:
  print(i)

print()

k = it.combinations(numbers, 3)
for i in k:
  print(i)

print()

k = it.combinations(twrd, 2)
for i in k:
  print(i)
