# itertools product function examples by GranD_MasTeR
import itertools as it

letter = ['a', 'b', 'c', 'd', 'e']
numbers = [0, 1, 2, 3, 4]
twrd = ['hi', 'bye']

h = it.product(numbers, repeat=3)
for i in h:
  print(i)

h = it.combinations_with_replacement(numbers, 3)
for i in h:
  print(i)
