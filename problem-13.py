n = int(input())
records = []
for _ in range(n):
    name = input()
    score = float(input())
    records.append([name, score])

second = sorted(set(s for _, s in records))[1]
for name in sorted([name for name, sc in records if sc == second]):
    print(name)