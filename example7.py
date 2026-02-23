scores = [10, 20, 4, 45, 99, 99]

highest = max(scores)
second = None

for s in scores:
    if s != highest:
        if second is None or s > second:
            second = s

print("Second highest:", second)