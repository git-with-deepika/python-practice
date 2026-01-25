f = open("data.txt", "r+")

print("Old content:")
print(f.read())

f.write("\nNew line added using r+ mode")

f.close()