m = [("chethan", 20, 30), ("john", 40, 50)]

print(m[1])

file = open("writingintocsvfile.csv", "w")
file.write("Name, Age, Weight")
for n in range(len(m)):
    file.write('\n')
    for k in range(len(m[1])):
        file.write(str(m[n][k]))
        file.write(',')
file.close()