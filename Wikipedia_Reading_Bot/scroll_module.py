import time

# scroll on page step_number times 
def scroll_x_time( browser, step, x ):  
    state = 0
    x = int( input( "step_number : " ) )
    
    height = browser.execute_script("return document.documentElement.scrollHeight")
    print( " total height : ", height )
    
    for i in range( 0, x ):  
        print( state )
        browser.execute_script("window.scrollTo(" + str( state )  + "," + str( state+step ) + ")")        
        state += step
        time.sleep( 8 )
    
    
# scroll end of the page 
def scroll_end_of_page( browser, step ):  
    state = 0
    
    height = browser.execute_script("return document.documentElement.scrollHeight")
    print( " total height : ", height )
    
    while state <= height:
        print( state )
        browser.execute_script("window.scrollTo(" + str( state )  + "," + str( state+step ) + ")")        
        state += step
        time.sleep( 8 )