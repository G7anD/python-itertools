# itertools dropwhile function examples by GranD_MasTeR
import itertools as it


def shart(n):
    if(n >= 2):
        return True
    else:
        return False


numbers = [3, 2, 1, 0, 3, 4, 5]

nat = it.dropwhile(shart, numbers)
for i in nat:
    print(i)
# 1
# 0
# 3
# 4
# 5
