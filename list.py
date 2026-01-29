a=[1,2,3,6,7,8]
print("Print list with default comma separator :")
print(a)

print("Print list with * :")
print(*a)

print("Print list with line separator (\\n) :")
print(*a, sep="\n")

print("Print list with comma (,) :")
print(*a, sep=",")
