# itertools accumulate function examples by GranD_MasTeR
import itertools as it
import operator as op

numbers = [3, 2, 1, 5, 3, 4, 5]

nat = it.accumulate(numbers)

print(list(nat))  # [3, 5, 6, 6, 9, 13, 18]

nat2 = it.accumulate(numbers, op.mul)
print(list(nat2))  # [3, 6, 6, 30, 90, 360, 1800]
