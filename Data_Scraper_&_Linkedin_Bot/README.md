# LinkedIn Bot & Data Scraping 
 
Linkedin Bot which select and add the people according to given keywords.


### Dependencies 

This bot is use this language, libraries and driver :

 - Python 3.8
 - Pandas 1.0.5
 - Selenium 3.141.0
 - Webdriver


 ### Installation
 
 To install this packages run the python installation instruction below in the command line :
  
```python
pip install -U selenium pandas 

```
To install chromedriver 

1. Go to chrome://settings/help and find out which is your Chrome's version
2. Go to https://chromedriver.chromium.org/downloads and find the latest version which supports your Chrome's version.
3. Download the one for your O.S.
4. Pick the executable and put in drivers' folder.
5. Replace and rename the executable with one that was already inside driver's folder depending on your O.S.
 
And check the dependencies :

```python
import pandas
import selenium
from selenium import webdriver

print( pandas.__version__)
print( selenium.__version__)
print( webdriver.__version__)
```

### Working Of Bot : 

At the beginning there are 4 steps before access the data paart.

1- Gets user information ( email and password ) and get number of people to be scanned.

2- Goes to website url.

3- Logins with user information.

4- Passes to the network section on the linkedin.


### Accessing & Selecting Data :

1- Accesses the data of in the suggestions people section.

2- Pulls the data including name and role of these people .

3- Selects the people according to keywords.

4- If the people is selected, bot adds this people as a new connection.

5- Shows selected people informations( name - role ).

6- When the finish of scan, shows the number of added people.

7- Saves this informations as a csv file.  

### A Little Optimization :

Search function in the code :

```python
def search( con, keys ):
    for c in con:    
        if  c in keys: 
            return True   

search( content_sp, key_word )
```
This function can be defined in one line with list comprehension method :

```python
search_one_line = bool( [ True for c in content_sp if c in key_word ] )

search_one_line
```
If the scraped data (role information) include one of the keywords both of these ways return "True" value. 

### ***Example Work***

For this keyword :

```python
 key_word = ['Human','Software','HR','Leader','Manager','Founder','Recruitment','Machine Learning','Data','Vision', ]
 
```
The csv file generated like this (created by mockaroo for in terms of data security) :

[data.csv](https://github.com/esencgr/Python_Projects/blob/master/Data_Scraping/data.csv)

![Screenshot from 2020-10-09 18-25-36](https://user-images.githubusercontent.com/32637622/95602178-33aacd00-0a5d-11eb-9b3f-ac91d968de0d.png)
