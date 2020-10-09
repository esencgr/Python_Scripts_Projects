# website = "https://www.google.com"
# course  = "Python: Hero to Zero Course"

# # lengt of "course" string
# print( len( course ))

# # pull "www" and "com " in the "website" string 
# print( website[ 8:11 ] )
# print( website[ -3: ] )

# l = len( website )
# print( website[ l-3:l ] )

# # first 15 and last 15 char in website str
# print( course[ :15 ] )
# print(course[ -15: ] )

# # reverse course 
# print( course[ :: ] )
# print( course[ ::-1 ] )

# # -----------------------------------
# # change the 'w' to 'W' 
# s = "Hello world"
# # s[ 6 ] = "W"
# s = s[ 0:6 ] + "W" + s[ -4: ]
# print( s )

# # -----------------------------------
# # delete start and end space  in the ' Hello World ' string
# s = " Hello World ".strip()
# s = " Hello World ".lstrip()
# print( s )
# s = " Hello World ".rstrip()
# print( s )


# #-----------------------------------
# # delete except google  
# website = "https://www.google.com"
# course  = "python HERO"

# s = website.lstrip( '/:psth' )
# print( s )

# s = website.strip( '/:psthw.com' )
# print( s )

# # all character lowercase and uppercase 
# s = course.lower()
# print( s ) 

# s = course.upper()
# print( s ) 

# how many "o" in websites
# s = website.count("o")
# s = website.count("o", 0, 10 )
# print( s )

# # -----------------------------------
# website = "https://www.google.com"
# course  = "python HERO"

# # is there "com" in website 
# f = website.find( "com" )
# print( f )

# f = website.find( "com", 0, 10 )
# print( f )

# f = website.index( "com" ) # right (rindex)left support
# print( f )

# # replace all "space" char with "-" char in the course  
# s = course.replace( " ","-")
# print( s )

# # isalpha isdigit ?
# s = course.isalpha()
# print( s )

# s = course.isdigit()
# print( s )



