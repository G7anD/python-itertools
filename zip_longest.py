# itertools zip_longest function examples by GranD_MasTeR
import itertools as it

for i in list(it.zip_longest(range(10), range(10, 0, -1))):
    print(i)

# (0, 10)
# (1, 9)
# (2, 8)
# (3, 7)
# (4, 6)
# (5, 5)
# (6, 4)
# (7, 3)
# (8, 2)
# (9, 1)
