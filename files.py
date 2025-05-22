fp = open("text.txt", "r")

print(fp.read())
n = 0
fp.seek(n)
print(fp.read())