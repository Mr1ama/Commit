nums = [-3, 5, 2, -8, 7, 4, -1]

res = [x * 2 for x in nums if x > 0]

print(res)


orders = ["pizza", "burger", "pizza", "sushi", "pizza", "burger"]

stats = {}

for item in orders:
    stats[item] = stats.get(item, 0) + 1

fin = [y for y in stats if y > 1]

for name, val in stats:
    print(fin)