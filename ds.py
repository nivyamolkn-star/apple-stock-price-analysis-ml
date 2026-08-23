import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data={
    'Name':['Bob','Alice','charile'],
    'Age':[20,21,22],
    'marks':[90,95,100]

}
student=pd.DataFrame(data)

print("student",student)

plt.figure(figsize=(6,12))
plt.bar(student['Name'],student['marks'],color='green')
plt.title("student")
plt.xlabel('Name')
plt.ylabel('Marks')
plt.grid(axis='y')
plt.show()