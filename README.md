# midtrans_test
Midtrans Interview Test


Here's the guide so you could run the test too.
Let me clarify some things before I start :
### All the guide that I wrote here belong to their respective ownership, nothing is original here, I only wrote what I do and follow through all the guide, and the time I wrote this guide, I haven't successfully automate the case 100% successfully, I have been trying with all I have and all the time I have, but here is the result. Thanks for everyone who wrote everything prior to me. ###

Now, these are the tools that I use to do the automation test :
1. Python scripting language
2. Splinter for the automation,
3. Using Selenium as the base

Before we going into the automation test, we need to install python first, **you can skip this step if your PC already installed python*

You can download the binary or windows config from here https://www.python.org/downloads/release/python-364/
*I'm using python 3.5.2*
Just download the executable installer for the easy installation on Windows. **I'm a windows user*

Now for the second step, we can install splinter and selenium at the same time
*to begin this step you need to make sure, that you have already installed pip via python setup, if you don't have pip go here https://pip.pypa.io/en/stable/installing/ *

you can follow the steps from here http://splinter.readthedocs.io/en/latest/install.html to install splinter
*Or*
1. Open command promt
2. type 'pip install splinter'
3. enter
4. wait through the process of installation

Last step before you can run the automation test, you need to install the respective browser WebDriver,
In this case, I'm using Chrome.
here is the guide provided by splinter : http://splinter.readthedocs.io/en/latest/drivers/chrome.html

If you are using windows, you need to assign the chromedriver to the system PATH,<br>
you can download the chromedriver from :https://sites.google.com/a/chromium.org/chromedriver/downloads</br>
If you do not know how to set up system PATH, you can look it up here :
read here http://msdn.microsoft.com/en-us/library/ms682653.aspx
OR
1. Right Click on 'My Computer' 
2. Select Advanced System Settings
3. Click Environment Variables
4. navigate to variable 'Path'
5. Click Edit
6. Click New
7. Add the system path to your chromedriver installation path/folder
8. Click OK
9.Don't forget to restart your PC, so the changes take effect

Now, you can run the code that I provide here, just download it to your computer
navigate to the folder containing the code using cmd
and type

python <program name>
  Ex : python testcase2.py
  picture example :
  https://drive.google.com/open?id=1lBuaw1kVRyB9td9FL8jtc5rHQtPOs6uJ
  
  Enter , and voila, just wait and see that the automation test running :)
  
  Note :
  1. testcase1.py is a simple test to show the automation is working
  2. testcase2.py is the No. 3 Answer, automation for demo.midtrans.com
    sadly, the automation is not 100% completed, and I'm stuck in some element.
