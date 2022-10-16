import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

# i for iteration, l for laptop, thus also why the "filecontent" has a l at the end
with open('iteration150LAPTOP.csv', 'r') as file:
    file_contentl = list(csv.reader(file, delimiter=","))

il = np.array(file_contentl).astype(float);

# i for iteration, v for Virtual Machines, thus also why the "filecontent" has a v at the end
with open('iteration150vm.csv', 'r') as file:
    file_contentv = list(csv.reader(file, delimiter=","))

iv = np.array(file_contentv).astype(float);

# i for iteration, d for docker, thus also why the "filecontent" has a d at the end
with open('iteration150docker.csv', 'r') as file:
    file_contentd = list(csv.reader(file, delimiter=","))

id = np.array(file_contentd).astype(float);

df = pd.DataFrame({'Number of iterations': il[0],'Time of execution': il[1]});
df2 = pd.DataFrame({'Number of iterations': iv[0],'Time of execution': iv[1]});
df3 = pd.DataFrame({'Number of iterations': id[0],'Time of execution': id[1]});
fig=plt.figure();

for frame in [df, df2,df3]:
    plt.plot(frame['Number of iterations'],frame['Time of execution'])

plt.xlabel('Number of iteration (150)');
plt.ylabel('Time of execution');
plt.legend(["Laptop","VM","Docker"]);
plt.title('Time of execution for multiplacation of matrix for 150 iterations');
plt.show();