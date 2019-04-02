# itertools count function examples by GranD_MasTeR
import itertools as it

for k in it.count(7):
  print(k, end=' ')
  if k >= 17:
    break
 # 7 8 9 10 11 12 13 14 15 16 17

print('\n')

for i in it.count(5, 5):
  print(i, end=' ')
  if i == 50:
    break
 # 5 10 15 20 25 30 35 40 45 50
