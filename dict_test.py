dict1 = {'2: Nick', '1: Usein'}
dict2 ={'1: Max', '2: Nick'}
dict3 ={'2: Max', '3: Nick', '1: Usein'}

all_dicts = {}

all_dicts.setdefault('1', []).append(dict1)
all_dicts.setdefault('1', []).append(dict2)
all_dicts.setdefault('1', []).append(dict3)

for k, v in all_dicts.items():
    for i in v:
        print(i)