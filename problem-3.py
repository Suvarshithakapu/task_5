s = input()
pos, char = input().split()
pos = int(pos)
new_s = s[:pos] + char + s[pos+1:]
print(new_s)