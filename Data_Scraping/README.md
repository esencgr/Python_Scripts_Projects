# LinkedIn Bot & Data Scraping 
 
Linkedin Bot which select and add the people according to given keywords.


### Dependencies 

*This bot is use this language, libraries and driver:*

 - Python 3.8
 - Pandas 1.0.5
 - Selenium 3.141.0  
 - Webdriver


 ### Installation
 
 *To install this packages run the python installation instruction below in the command line:*
  
 ```bash
pip install -U selenium pandas 

```
*You can install chromedriver :*

1. Go to chrome://settings/help and find out which is your Chrome's version
2. Go to https://chromedriver.chromium.org/downloads and find the latest version which supports your Chrome's version.
3. Download the one for your O.S.
4. Pick the executable and put in drivers' folder.
5. Replace and rename the executable with one that was already inside driver's folder depending on your O.S.
 
 *And check the dependencies :*

 ```bash
import pandas
import selenium
from selenium import webdriver

print( pandas.__version__)
print( selenium.__version__)
print( webdriver.__version__)
```

### Working Of Bot : 

At the beginning there are 4 steps before access the data paart.

1- Get user information ( email and password ) and get number of people to be scanned.

2- Go to website url.

3- Login with user information.

4- Pass to the network section on the linkedin.


### Accessing & Selecting Data :

1- Accesses the data of in the suggestions people section.

2- Pulls the data including name and role of these people .

3- Selects the people according to keywords.

4- If the people is selected, bot adds this people as a new connection.

5- Shows selected people informations( name - role ).

6- When the finish of scan, shows the number of added people.

7- Saves this informations as a csv file.  




