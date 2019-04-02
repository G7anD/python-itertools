# itertools chain function examples by GranD_MasTeR
import itertools as it

print(list(it.chain('xyz', '123')))  # ['x','y','z','1','2','3']

print(list(it.chain(['qwe', 'rty'])))  # ['qwe','rty']

print(list(it.chain(['qwe'], ['rty'])))['qwe', 'rty']
