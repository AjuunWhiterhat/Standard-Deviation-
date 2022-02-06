import csv



with open("HeightWeight.csv",newline="") as f:
    Reader = csv.reader(f)
    Data = list(Reader)

Data.pop(0)

newData = []

total = 0

for i in range(len(Data)):
    num = Data[i][1]
    newData.append(float(num))

elements = len(Data)

for x in newData:
    total += x

mean = total / elements
print("Mean is : "+str(mean))

import pandas as pd
import plotly.express as px
df = pd.read_csv("HeightWeight.csv")
graph = px.scatter(df,x="Index",y="Height(Inches)")
graph.update_layout(
    shapes = [
        dict(
            type="line",
            y0 = mean,
            y1 = mean,
            x0 = 0,
            x1 = elements
        )
    ]
)

graph.show()

