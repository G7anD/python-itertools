# itertools filterfalse function examples by GranD_MasTeR
import itertools as it


def shart(n):
    if(n > 3):
        return True
    else:
        return False


numbers = [0, 1, 2, 3, 4, 5, 6, 3, 1, 3, 6, 8]

result = it.filterfalse(shart, numbers)
for i in result:
    print(i)
# 0
# 1
# 2
# 3
# 3
# 1
# 3
