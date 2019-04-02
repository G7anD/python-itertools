# itertools cycle function examples by GranD_MasTeR
import itertools as it

velo = it.cycle([7, 8, 9])

print(next(velo))  # 7
print(next(velo))  # 8
print(next(velo))  # 9
print(next(velo))  # 7
print(next(velo))  # 8
print(next(velo))  # 9
print(next(velo))  # 7

print()

velo2 = it.cycle(['red', 'green', 'blue'])
print(next(velo2))  # red
print(next(velo2))  # green
print(next(velo2))  # blue
print(next(velo2))  # red
print(next(velo2))  # green
print(next(velo2))  # blue
print(next(velo2))  # red

print()

velo3 = it.cycle(['true', 'false'])
print(next(velo3))  # true
print(next(velo3))  # false
print(next(velo3))  # true
