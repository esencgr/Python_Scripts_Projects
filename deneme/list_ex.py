# # 1- createa list "Bmw. Mercedes, Opel, Mazda"
# cars = [ "Bmw", "Mercedes", "Opel", "Mazda" ]
# print( cars )

# # 2- list size ?
# sz = len( cars )
# print( sz )


# # 3- first and last element of list
# print( cars[ 0 ], cars[ sz -1 ])


# # 4- change "Mazda" with "Toyota"
# cars[ -1 ] = "Toyota"  
# print( cars )


# # 5- is "Mercedes" a list element
# res = cars.index( "Mercedes" ) 
# print( res )
# res = "Mercedes" in cars 
# print( res )


# # 6- value of the -2 index of the list
# res = cars[ -2 ]  


# # 7- first 3 element of list
# res = cars[ 0:3 ]
# res = cars[ :3 ]
# print( res )


# # 8- change last two elemnt with the "Toyota" and "Renaukt"
# cars[ -2: ] = "Toyota", "Renault"
# res = cars


# # 9- add "Audi" "Nissan"
# res = cars + [ "Audi", "Nissan" ]
# cars = cars + [ "Audi", "Nissan" ]
# print( cars )


# # 10- delete the last elemnt of list
# del( cars[ -1 ] )
# print( cars )


# # 11- reverse list
# cars.reverse()
# print( cars )

# res = cars[ : : -1 ]
# print( res )


# # 12- create a list like that 
#     student_a = cgr 2010, (70,60,70)
#     student_b = sena 1999, (80,80,70)
#     student_c = ahmet 1998, (80,70,90)

# # write a list 
  
# stu_a = [ "cgr", 2010, [ 70,60,70 ] ]
# stu_b = [ "sena", 1999, [ 80,80,70 ] ]
# stu_c = [ "ahmet", 1998, [ 80,70,90 ] ]

# s = stu_a + stu_b + stu_c
# print( s )    

# res = stu_a[ 0 ]
# res = stu_c[ 2 ][ 2 ]

# avr = ( stu_a[ 2 ][ 0 ] + stu_a[ 2 ][ 1 ] + stu_a[ 2 ][ 2 ] ) / 3 
# res = ( f"{ stu_a[ 0 ] } is { 2020 - stu_a[ 1 ] } years old and note avr = {avr:.2f}" ) 
# # res = ( "{} is {} years old and note avr {:.2f}".format( stu_a[ 0 ], ( 2020 - stu_a[ 1 ] ), avr ))
# print( res )


# names = [ "Ali", "Yağmur", "Hakan", "Deniz" ] 
# years = [ 1998, 2000, 1998, 1987 ]

# #1- add cenk name to the end of names
# names.append( "Cenk" )
# print( names )


# #2- add sena name to the start of names  
# names.insert( 0, "la" )
# names.insert( -1, "le" )
# names.insert( len( names ), "lo" )
# print( names ) 


# #3- delete deniz name to the names
# names.remove( "Deniz" )
# names.pop()   # last element del
# print( names )


# # 4- what is deniz name 's index value 
# res = names.index( "Deniz" )
# print( res )


# # 5- is ali a element of names ?
# res = "Ali" in names 
# print( res )


# # 6- reverse names 
# print( names )
# res = names.reverse()
# print( names ) 


# # 7- sort names alphabetichal order
# names.sort()
# print( names  )


# # 8- sort years 
# years.sort()
# print( years )


# # 9- str = "Dacia, Chaevrolet" covert to list
# str = "Dacia, Chaevrolet" 
# res = ste.split(',') # res = list(str)
# print( res )


# # 10- years min max 
# mn = min( years )
# print( mn )

# mx = max( years )
# print( mx )


# # 11- how many 1998 in years ?
# c = years.count( 1998 )
# print( c )


# # 12- delete all elemnts in years 
# years.clear()
# print( years )


# # 13- put in a list that  the three value entered by user
# cars = []
# for i in range ( 0,3 ):
#     car = input( "enter car: ")
#     cars.append( car )
# print( cars ) 
 
