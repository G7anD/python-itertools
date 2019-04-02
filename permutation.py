# itertools permutations function examples by GranD_MasTeR
import itertools as it

letter = ['a', 'b', 'c', 'd', 'e']
numbers = [0, 1, 2, 3, 4]
twrd = ['hi', 'bye']

k = list(it.permutations(letter, 2))
for i in k:
  print(i)

print()

k = list(it.permutations(numbers, 2))
for i in k:
  print(i)

print()

k = list(it.permutations(twrd, 2))
for i in k:
  print(i)
