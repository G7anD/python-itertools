# itertools starmap function examples by GranD_MasTeR
import itertools as it

st = it.starmap(pow, [(0, 1), (1, 2), (2, 2)])  # [0, 1, 4]
print(list(st))

stt = it.starmap(pow, list(zip(range(5), it.repeat(2, 3))))  # [0, 1, 4]
print(list(stt))
