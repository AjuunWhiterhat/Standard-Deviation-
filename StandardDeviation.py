import math 
import csv


with open("data.csv") as f:
    Reader = csv.DictReader(f)
    fileData = list(Reader)

fileData.pop(0)
data = fileData[1]

print(data)

def mean(data):
    n = len(data)
    total = 0

    for x in data:
        total+= int(x)
    
    mean = total / n
    return mean

squared_list = []

for number in data:
        a = int(number) - mean(data)
        a = a**2
        squared_list.append(a)

sum = 0
for i in squared_list:
    sum =sum + i

result = sum/ (len(data)-1)

std_deviation = math.sqrt(result)

mean(data)





