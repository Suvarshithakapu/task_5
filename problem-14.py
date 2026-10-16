n = int(input())
marks = {}
for _ in range(n):
    line = input().split()
    marks[line[0]] = list(map(float, line[1:]))
query = input()
avg = sum(marks[query])/len(marks[query])
print(f"{avg:.2f}")