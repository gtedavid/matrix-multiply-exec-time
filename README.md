# matrix-multiply-exec-time - Lab 1

## Task - Develop & test a code for monitoring time execution of matrix multiplication on 3 different platforms (Laptop/VM/Container)

## Notice

   1. This python code was developped with the help of a few websites for a Lab.
Those sites are mentioned in the code.

- _Function 1_, line 10, originates from <https://stackoverflow.com/questions/17760877/getting-safe-user-input-in-python>
   It was slightly modified to be used in this code
   From response edited on June 16, 2020 at 9:12, answered July 20, 2013 at 10:05 by ___TerryA___

- _Function 2_, line 23, is from <https://geekflare.com/multiply-matrices-in-python/>
   It was slightly edited for the use of the program
   From "3 Ways to Multiply Matrices in Python", By ___Bala Priya C___ in Development on July 1, 2022

- _Plotting syntax_, line 81, inspired from Example 2 on <https://www.educba.com/pandas-dataframe-plot/>

_Please note that I'm not in anyway responsible for malfunctioning of the use of Python, abusive number entry in the program or any of the librairies used._

If the authors of the above posts would like to see their content be deleted from this program, feel free to provide any proof of it being yours.

## Use / licencing not set

Please feel free to use this program if you need it.
If you use it in any project, hand-in lab, etc, please credit the work done by others and what I did, as I do my best to give credit to the work of others that help me.

1. Librairies used in this program :

- numpy
- pandas
- matplotlib

## About the code

### Installation and use

Before launching this program make sure __Python 3.10__ is downloaded, and you have installed the packages of the librairies mentioned above with pip.

   1. Windows
   `pip install name_of_a_package` be sure to replace `name_of_a_package` with one of the above packets.
   Once it's done, use the IDE of your choice to execute the code, be sure to install any extensions or elements you may need to execute this Python code.

   1. Debian (Linux)
   To install Python on Linux, you can refer to one of the tutorials posted on the web.
   This one was used : <https://computingforgeeks.com/how-to-install-python-on-debian-linux/>
   `sudo python3.10 pip name_of_a_package` be sure to replace `name_of_a_package` with one of the above packets.
   On Linux I used this tutorial to install Visual Studio Code <https://code.visualstudio.com/docs/setup/linux>
   
   1. Docker
   _More info to come once technical difficulties are sorted out_

### Requirements

For the time being, you need a graphical interface to use this program.
The recommended/ideal OS and specs would be the following:

   1. Windows 10/11 32/64bits with:

   - sufficient memory usage, around 4 to 8 GB, tested with 16GB (some already in use)
   - a processor running on 2.30 GHz basis up to 4.50 GHz
   - any hardware, as long as there is space available.

   1. Debian 11.5.0 64 bits with Graphical Interface (VM)
   - sufficient  memory usage, around 4Gb or more, tested with 2GB
   - a processor running on 2.30 GHz basis up to 4.50 GHz
   - any hardware, as long as there is space available.

Please avoid entering big numbers for this program; 150 was the max tested with.
Your computer may be impacted if you voluntarily input a higher number.
Note that depending on your specs wheter it be VM, laptop or container, the execution time varies.
The above specs are close to the ones for which the program was tested on.

### What does this code do ?

This codes computes the execution time on a diagram for n iteration and until size n for each matrix.
It will ask for the number of iterations you want to go for.

Please avoid entering big numbers for this program; 150 was the max tested with.
The est. time of execution for 150 iterations is a min to 3 min.
Your computer may be impacted if you voluntarily input a higher number.
