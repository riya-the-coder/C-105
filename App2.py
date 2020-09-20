import csv
import math
with open("class1.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
data=file_data[0]
def mean(data):
    total_marks=0
    total_entries=len(data)

    for marks in data:
        total_marks+=int(marks)

    mean=total_marks/total_entries
    print("mean",str(mean))

sqaurelist=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    sqaurelist.append(a)

sum=0
for i in sqaurelist:
    sum=sum+i

result=sum/(len(data)-1)
std_deviation=math.sqrt(result)
print(std_deviation)
