d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

new_d = {k: v for k, v in d.items() if v > 2}

print(new_d)