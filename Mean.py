import csv 

with open("HeightWeight.csv",newline="") as f:
    Reader = csv.reader(f)
    fileData = list(Reader)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))


n = len(newData)

total = 0

for x in newData:
    total += x

mean = total / n

print("mean/average is : "+str(mean))


