s = input()
kevin = stuart = 0
for i in range(len(s)):
    if s[i] in 'AEIOU':
        kevin += len(s)-i
    else:
        stuart += len(s)-i

if kevin > stuart:
    print(f"Kevin {kevin}")
elif stuart > kevin:
    print(f"Stuart {stuart}")
else:
    print("Draw")