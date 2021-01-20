from selenium import webdriver
import pandas as pd 
import time

mail = input( "mail : " )
pwd = input( "password : " )
number_of_scans = int( input( "how many people do you want scan : " ))
tm = 3 

# start webdriver
browser = webdriver.Chrome()

# get source code
linkedin_url = "https://www.linkedin.com/"
browser.get( linkedin_url ) 
time.sleep( tm )

# click login button 
log_in = browser.find_element_by_class_name( 'nav__button-secondary' )
log_in.click()
time.sleep( tm )

# enter your password end mail
usr = browser.find_element_by_xpath( "//*[@id='username']" )
pss = browser.find_element_by_xpath( "//*[@id='password']" )

# enter username and psw and click 
usr.send_keys( mail )
time.sleep( tm )
pss.send_keys( pwd )
time.sleep( tm )

# click sign in
log = browser.find_element_by_xpath("//*[@id='app__container']/main/div[2]/form/div[3]/button")
log.click()
time.sleep( tm )

# click my network tab
my_net = browser.find_element_by_xpath('//*[@id="ember26"]')
my_net.click()
time.sleep( tm*2 )

# data scraping part
key_word = ['Human','Software','HR','Leader','Manager','Founder','Recruitment',
            'Machine Learning','Data','Vision',"Python", "C++"]

# def search( con, keys ):
#     for c in con:    
#         if  c in keys: 
#             return True   

def selection( key_word, browser ) :
    count = 0
    d = dict()
    data = dict()
    lst_name = list()
    lst_role = list()
    
    for i in range ( 0, number_of_scans ):
        content = browser.find_element_by_class_name('discover-person-card__occupation')
        time.sleep( tm ) 
        content_sp = content.text.split()        

        search_one_line = bool( [ True for c in content_sp if c in key_word ] )
        
        if( search_one_line ):   # for search function -> search( content_sp, key_word )
            print( )
            name = browser.find_element_by_class_name('discover-person-card__name')
            print( "* " + name.text + " - " + content.text)

            lst_name.append( name.text )
            lst_role.append( content.text )
            
            d = { 'names' : lst_name, 'roles' : lst_role }
            data.update( d ) 
            time.sleep( tm )
      
            button = browser.find_element_by_class_name('full-width')
            button.click()
            time.sleep( tm )
            
            exit_b = browser.find_element_by_class_name('artdeco-card__dismiss')
            exit_b.click()
            time.sleep( tm )
            count = count + 1
                    
        else:
            exit_b = browser.find_element_by_class_name('artdeco-card__dismiss')
            exit_b.click()
            time.sleep( tm )

    print( f"\ntotal new connection = {count}" )
    
    # Creating to dataframe from data dictionary
    df = pd.DataFrame( data, columns = ['names', 'roles'] )        
    print( df )
    
    # # Saving the data into a csv file,
    df.to_csv("data_1.csv",index=False) 
    

selection(key_word, browser)

#close browser
browser.close()




