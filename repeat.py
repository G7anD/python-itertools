# itertools repeat function examples by GranD_MasTeR
import itertools as it

tak = it.repeat(2)

print(next(tak))  # 2
print(next(tak))  # 2
print(next(tak))  # 2
print(next(tak))  # 2
print(next(tak))  # 2

print()

tak2 = it.repeat(2, 3)  # 3 times

print(next(tak2))  # 2
print(next(tak2))  # 2
print(next(tak2))  # 2
print(next(tak2))  # err
