Introduction:
-------------

Firstly, congratulations for showing the courage to try out something new. Jupyter Notebook is an
extremely powerful tool as you will soon realize. You are running this on the JupyterHub instance
that I have set up on Texas Advanced Computing Center (TACC). Even though you will be working on
your laptop (seemingly), the code is actually running on a 44-core 120 GB RAM machine in Texas.
This should in principle be able to handle a large number of you working at the same time. If we 
see any issue, then I can request for more resources from them.

Jupyter Notebook: Jupyter notebook is an open-source Web application that allows you to create and 
share documents that contain live code, equations, visualizations and narrative text. Or in other
words the perfect tool to do collaborative work, like Lab experiment, research, or even class 
projects. If you want to learn more about Jupyter visit their home page here: https://jupyter.org

This is a good opportunity for you to use Jupyter Notebook in action in this lab, because you will
find most of the code skeleton ready. In the beginning you will only have to change the names of the 
files, name of the variables etc. However, you will have read the lines carefully to know what you
need to replace. I have put markers where you should change things and what you should avoid from
changing unless you know what you are doing. Please meticulously follow the instruction in the
notebook.

A jupyter notebooks is composed of many cells. Each cell can be used for two purpose, it can 
either be used to write code snippets, or it can be used to write text. By default every cell is
opened in the code snippets format. You can select from the drop-down menu at the top to change it
to markdown format, where you can write text. In the markdown format you can start any sentence
with # and then a space to switch on markdown formatting.

If a cell is in code format, you can still use the # symbol to comment on a code. This is very 
useful to record important information about the code inside the code itself. This is a feature
that can be used in Python scripts as well, and is not unique to Jupyter. You will find plenty of
comments with # in the notebook that you will be working on. PLEASE READ THESE EXTREMELY CAREFULLY.

In Jupyter, you can run a cell by pressing Shift + Enter. If you want to run a cell and insert
a cell right after that then press Alt + Enter (Option + Enter for Mac). 



Instruction:
------------
Firstly, you need to understand what is required of you. The first part of the experiment has
already been done. You are required to do the remaining two parts. For this you will need the 
equipments delineated on Canvas. Make sure to measure the angle using the phone app if possible.
The next thing you need to be very careful is the way you enter the data. Follow the example shown
in the existing `slide_trials_first_angle.txt` in this directory. You need to make sure that there
are 11 columns in this file, the first one being the trial number. The next 10 columns should be 
the 10 different lengths of the sliding in the experiment. The first of these columns should be 
the longest length, and each column should be shorter lengths than the next. It is very IMPORTANT
that you follow this structure. If you don't the code will not work the way it is supposed to, and
your results will be wrong. Following the structure is not be difficult, it is just that you need to
be mindful of it. If you change the structure of the files then you will have to write your own 
plotting scripts. 

In the "Measurement of the angle of the plank" section, you will find the first place where you 
will have to do something. The first cell is for the experiment I conducted during the demo. Read
it to make sure that you are understanding it. Run the cell by pressing Shift + Enter, then move 
to the next cell. In this cell you will have to put the angles of the new inclination. Remember,
to record the values in the list named `angles`. Note that the place holder values of -1 should
be changed. Repeat the same for the next cell, where you enter the results from the third angle.

Now that you have recorded the angles, we are ready to do the actual experiment. Start the 
experiment with the largest value of the slide (which was an incline length of 105 cm). Conduct the
measurement for 5 sets, and immediately enter in the txt file. You might want to do the recording
locally on notepad, or something like that and then copy-past it to the file on JupyterHub. 
Make sure you enter this data in the right file, `slide_trials_second_angle.txt`. Run the cells to
progress through the analysis. I expect many of you to have some problem at this stage. That is 
okay, just reach me out on Slack, we will figure it out. But, make sure to carefully read all 
the commented lines in the cells. Many of the problems will be solved there. 
Repeat this experiment for the third angle. Here, I left it entirely up to you to clone whatever
I have done earlier. The hope is that after reading the first one, and partially doing the second 
one, you will be in a position to do the third one on your own. If you face problems reach me out.

Now it is time to make some graphs. If up until now you have run through the code, the plotting 
code should run just fine. If not, then we will look into it. One place where the plotting code
can fail is if you did not use the right name for the third observation. That can happen because I 
did not provide any skeleton for you there. But if you see any error message in the plotting part 
of the notebook, make sure to read it carefully and see if is complaining about things like `t3` 
or `x3`, then you know that you have used wrong variable names. Go back and check the variable 
names I used for the first two observation, and you can just use that to guide you. If you are not 
able to figure it out, just ask me. 

If you have reached this far, the next cell should just run seamlessly, creating the average 
values of the value of g, and computing the fraction and rms errors. Note that there are many places 
where I have commented out the lines for the third angle. That is because you will have to do that 
experiment and then create the file for that, like one exists for the the first one. Once you have 
that you can uncomment these lines to run them and get the result for the third angle.

The final calculation of the standard deviation using the two angles needs to be done using the 
example of the first angle that I have put in the notebook. Copy these lines of code after 
inserting a cell below and then change the variable to the ones for the second and the third 
results.














