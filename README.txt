*** README FOR FINAL RELEASE***

We had a reoccuring and awful build issue that causes a Fatal Python Error and could not get it resolved before our final build date. 

I will leave the MinerFinal.zip in this drive to take a look at the code and run the program  
	Steps to play:
	- Open the project in PyCharm
        - Packages to download
		- PyQt5 version 5.14.2
		- PyQtWebEngine version 5.14.2
		- Pandas version 1.0.3
		- Plotly version 4.6.0
		- Dash version 1.10.0
 	- Navigate to Main.py
	- Run Main.py

To Test the Program 
- We wanted to make sure that anywhere that a user could give the system a value that we check it. 
	- Glossary section will return a helpful message that the item is not in the glossary
	- Buy area: Putting in invalid values will result in a message appearing
       		    Trying to buy more stocks than you can afford will give an error message
	- Sell area: Giving the system an incorrect transaction number will produce an error message
 	  	     Trying to sell more stocks than you have will produce an error message
	             Incorrect values will produce an error message
