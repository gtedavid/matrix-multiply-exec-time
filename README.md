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

#### Part 1 - General Use in the different environments

Before launching this program make sure __Python 3.10__ is downloaded, and you have installed the packages of the librairies mentioned above with pip.

   1. Windows
   `pip install name_of_a_package` be sure to replace `name_of_a_package` with one of the above packets.
   Once it's done, use the IDE of your choice to execute the code, be sure to install any extensions or elements you may need to execute this Python code.

   1. Debian (Linux)
   To install Python on Linux, you can refer to one of the tutorials posted on the web.
   This one was used : <https://computingforgeeks.com/how-to-install-python-on-debian-linux/>
   `sudo python3.10 pip name_of_a_package` be sure to replace `name_of_a_package` with one of the above packets.
   On Linux I used this tutorial to install Visual Studio Code <https://code.visualstudio.com/docs/setup/linux>

   1. Docker *
   `docker run -it dgefrei/cloudinfraserviceslab1` in a command prompt to install the image of the code and the OS. You'll need to have Docker (Desktop) installed, with WSL2 for example on which it can run. Note that once it finished installing, it will launch the program inside the container. Then you'll be asked to enter the number of iterations you want.
   
   Once you've entrered the desired number, the code will run inside the container. Once it is done, it will save the plot in a png file and display the average time of execution and the total time of executions for the multiplication of matrix. The container will then shut down. You'll just have to turn the container back on to copy the image file of the graph by typing  `docker cp <id_or_name_of_container>:/home/iteration<Number_of_iterations>.png <targert_path>` to save it to the folder you want.
   
   For other iterations, you will just have to do `docker exec -it <id_or_name_of_container> bash` and then launch the program situated in home folder by typing `python3 /home/Lab1.py`, and enter the number of iterations you want when prompted to. The program will give you the average time of execution and the total time of executions for the multiplication of matrix for the number of iterations you asked. Once more the image of the graph will be saved in the container. Outside of the container's command interface, you will be able to copy it like the previous one, the same way as mentioned previously.

* _Docker Desktop on Windows is used here. The program was not tested with other OS than Debian, Windows and Ubuntu._

#### Part 2 - Using the comparing python code

Please note that before launching this, you would have needed to put in the same folder as where these codes are located the following :

- all the iteration<number_of_iteration>LAPTOP.csv files;
- all the iteration<number_of_iteration>vm.csv files copied manually from the virtual machines;
- all the iteration<number_of_iteration>docker.csv files copied via command via a command prompt from the docker container.

If 30, 50, 80, 100 or 150 is not one of the numbers you want to try, be sure to change the files accordingly where the correspondig number appears.

Once the above is done, you'll just have to execute the file in your favorite python compiler, and see the result presented on the graph.
Please note that when this code was tested, no errors appeared.
Check that previous installations were done correctly.

### Requirements

For the time being, you need a graphical interface to use this program.
The recommended/ideal OS and specs would be the following:

   1. Windows 10/11 32/64bits with:

   - sufficient memory usage, around 4 to 8 GB, tested with 16GB (some already in use)
   - a processor running on 2.30 GHz basis up to 4.50 GHz
   - any hardware, as long as there is space available.

   1. Debian 11.5.0 64 bits with Graphical Interface (VM)

   - sufficient  memory usage, around 4Gb or more, tested with 2GB, than increased to 3GB for better experience.
   - a processor running on 2.30 GHz basis up to 4.50 GHz
   - any hardware, as long as there is space available.

   1. Docker - info variable

   - as long as you have one of the above specs available, and a correct internet connection, all is good.

Please avoid entering big numbers for this program; 150 was the max tested with.
Your computer may be impacted if you voluntarily input a higher number.
Note that depending on your specs wheter it be VM, laptop or container, the execution time varies.
The above specs are close to the ones for which the program was tested on.

### What does this code do ?

This codes computes the execution time on a diagram for n iteration and until size n for each matrix.
It will ask for the number of iterations you want to go for.

Please avoid entering big numbers for this program; 150 was the max tested with.
The est. time of execution for 150 iterations is a minute to 3 minute, though may vary depending on your computer.
Your computer may be impacted if you voluntarily input a higher number.
