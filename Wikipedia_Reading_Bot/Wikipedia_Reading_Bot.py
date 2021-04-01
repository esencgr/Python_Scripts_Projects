from selenium import webdriver
import time 
import scroll_module

step = int( input( "step : " ) )

# start webdriver

browser = webdriver.Chrome()

# get source code
viki_url = "https://tr.wikipedia.org/wiki/Vikipedi"
browser.get( viki_url ) 
time.sleep( 5 )

# scroll_module.scroll_x_time( browser,step, x )
scroll_module.scroll_end_of_page( browser, step )

#close browser
browser.close()
