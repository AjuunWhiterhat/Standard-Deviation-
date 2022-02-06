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

newData.sort()

if n%2==0:
    median1 = float(newData[n//2])
    median2 = float(newData[n//2-1])
    median = (median1 + median2)/2

else:
    median = float(newData[n//2])
    print(n)

print("Median : "+str(median))
