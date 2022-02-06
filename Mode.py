import csv 
from collections import Counter

with open("HeightWeight.csv",newline="") as f:
    Reader = csv.reader(f)
    fileData = list(Reader)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))


data = Counter(newData)
modDataforRange = {
    "50-60":0,
    "60-70":0,
    "70-80":0,
}

for height,frequency in data.items():
    if 50<float(height)<60:
        modDataforRange["50-60"]+=frequency
    elif 60<float(height)<70:
        modDataforRange["60-70"]+=frequency
    elif 70<float(height)<80:
        modDataforRange["70-80"]+=frequency
    
modRange,modFrequency = 0,0

for range,occ in modDataforRange.items():
    if frequency>occ:
        modRange,modFrequency = [int(range.split("-")[0]),int(range.split("-")[1])],occ

mod = float((modRange[0]+modRange[1])//2)

print(f"mod : {mod:2f}")
        




