# itertools dropwhile function examples by GranD_MasTeR
import itertools as it

roy = [
    {
        "name": "Eric",
        "city": "PY",
        "state": "DV"
    },
    {
        "name": "Davi",
        "city": "CP",
        "state": "DV"
    },
    {
        "name": "Otash",
        "city": "CS",
        "state": "DV"
    },
    {
        "name": "Java",
        "city": "JR",
        "state": "DV"
    },
    {
        "name": "Jaki",
        "city": "PP",
        "state": "DR"
    },
    {
        "name": "Muha",
        "city": "JS",
        "state": "KC"
    }
]


def ajr(o):
  return o["state"]


nat = it.groupby(roy, ajr)
for kal, group in nat:
  print(kal)
  for k in group:
    print(k)
  print()

# DV
# {'name': 'Eric', 'city': 'PY', 'state': 'DV'}
# {'name': 'Davi', 'city': 'CP', 'state': 'DV'}
# {'name': 'Otash', 'city': 'CS', 'state': 'DV'}
# {'name': 'Java', 'city': 'JR', 'state': 'DV'}

# DR
# {'name': 'Jaki', 'city': 'PP', 'state': 'DR'}

# KC
# {'name': 'Muha', 'city': 'JS', 'state': 'KC'}

print()

nat = it.groupby(roy, ajr)
for kal, group in nat:
  print(kal, len(list(group)))

# DV 4
# DR 1
# KC 1
