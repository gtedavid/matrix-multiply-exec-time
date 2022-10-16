import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
import csv

# Notice : Please red the ReadMe.md file link to the repo of this code before use.
# Code produced with the help of the links mentioned below by gtedavid

input1 = "";

# Function originating from https://stackoverflow.com/questions/17760877/getting-safe-user-input-in-python
# slightly modified to be used in this code
# edited Jun 16, 2020 at 9:12, answered Jul 20, 2013 at 10:05 by TerryA

def getNumeric(input1):
    while True:
        try:
            print("Please enter the number of iterations: ");
            res = int(input(input1));
            break;
        except ValueError:
            print("Please enter the number of iterations: ");
    return res;

# Function from https://geekflare.com/multiply-matrices-in-python/
# slightly edited for the use of the program
# "3 Ways to Multiply Matrices in Python", By Bala Priya C in Development on July 1, 2022
np.random.seed(27);
def multiply_matrix(A,B,i):
  global C
  if  A.shape[1] == B.shape[0]:
    C = np.zeros((A.shape[0],B.shape[1]),dtype = int);
    for row in range(i):
        for col in range(i):
            for elt in range(len(B)):
              C[row, col] += A[row, elt] * B[elt, col];
    return C;
  else:
    return "Sorry, cannot multiply A and B.";

# numerical input wanted
n = getNumeric(input1);



# Initiation of array for the timestamps and time count
timestamps = [];
timestamps_i = [];
# This was one of the test I did to fill in the first two values, 0 and 1 of the list

# timestamps.insert(0,0);
# timestamps_i.insert(0,0);
# timestamps.insert(1,0);
# timestamps_i.insert(1,0);

for i in range (2,n+1):
    # creating two random matrices of size i
    A = np.random.randint(1,10,size = (i,i));
    B = np.random.randint(1,10,size = (i,i));

    # creating an empty matrix 
    C = np.zeros((A.shape[0],B.shape[1]),dtype = int);

    # filling an empty matrix and taking the timestamps
    start_time = time.time();
    C = multiply_matrix(A,B,i);
    end_time = time.time();

    # print(i); # this was to give me an idea of when the execution stoped in case of an issue
    # print(f"Matrix C:\n {C}\n"); # this was to give me an idea of when the execution stoped in case of an issue
    
    timestamps_i.insert(i-2,i);
    # here we do -2 because the index of the list doesn't start at 2 but at 0, so it is shifted
    if i == 2:
        timestamps.insert(i-2,0+end_time-start_time);
        # first iteration, we don't have any data previously
    else:
        timestamps.insert(i-2,end_time-start_time);
        # 2nd and other iterations, we decrease i to have the correct index


df = pd.DataFrame({'Number of iterations': timestamps_i,'Time of execution': timestamps});
# Plotting syntax from https://www.educba.com/pandas-dataframe-plot/ Example 2

df.plot(x='Number of iterations', y='Time of execution');
print("Average time: ", sum(timestamps)/len(timestamps));
print("Total time of execution: ", sum(timestamps));
plt.savefig("iteration"+str(n)+".png");
# plotting the data
path_file_csv = str("iteration"+str(n)+"vm.csv");
with open(path_file_csv, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(timestamps_i)
    spamwriter.writerow(timestamps)

