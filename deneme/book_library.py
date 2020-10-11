# -*- coding: utf-8 -*-
import os 
book_list =  [ "dava", "beyaz diş" ]

menu = """

 --- MENU --- 
a -> add book 
d -> delete book 
s -> show book list 
q -> quit
       
       """
def show( books:list ):
    c = 0
    for b in books:
        c += 1
        print( f"{c} : {b}" ),
    print( "\n" )


def add( books:list ):
    b = input( "enter book name for add : " )
    books.append( b )   
    print( f"added '{b}' book to list" )
    show( books )
    
    print("plase enter for menu")
    input()


def delete( books:list ):
    show( books )
    b = input( "enter book name for delete : " )
    books.remove( b )
    print( f"removed '{b}' book to list" )
    
    print("plase enter for menu")
    input()


def check_list( books:list ):
    c = 0
    for b in books:
        c += 1
        print( f"{c} : {b}" )
    print("plase enter for menu")
    input()


while True: 
    os.system("clear")
    print( menu )
    show( book_list )

    ch = input( "enter your choise : " )
    
    if( ch == "a" ):
        add( book_list ) 
        
    elif( ch == "d" ):
        delete( book_list ) 

    elif( ch == "s" ):
        check_list( book_list )

    elif( ch == "q" or ch == "Q" ):
        print( "End ..." )
        break 
    
    else:
        print( "Wrong input. Try again !!" )



        