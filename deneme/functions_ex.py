# -*- coding: utf-8 -*-

# # 1- Gönderilen bir ifadeyyi belirtilen bir sayı kez ekrana bastıran fonksiyonu yazdırın
# def pr( s, n ):
#     print( s * n )
#     # for i in range( 0, n ):
#     #     print( s )
#
# word = input( "enter string : " )
# num = int( input( "enter num : " ))
# pr( word, num )


# # 2- Sınırsız sayıdaki parametreyi listeye çeviren fonksiyon
# def con_lst( *params ):
#     lst = list()
#     for param in params:
#         lst.append( param )
#     return lst

# new = con_lst( 1, 2, 3, 4, "hello", "cool" )
# print( new )


# # 3- Gönderilen iki sayı arası asal sayılar 
# def prime( n1, n2 ):
#     for num in range( n1, n2 ):
#         if( num > 1 ):
#             var = True 
#             for i in range( 2, num ):
#                 if( num % i == 0 ):
#                     var = False 
#             if ( var == True ):
#                 print( num )
# prime( 0, 30 )


# # 4- Kendisine gönderilen sayının tam bölenlerini listeye ekle yazdır
# def div( num ):
#     lst = list()
#     for i in range( 1, num + 1 ):
#         if( num % i == 0 ):
#             lst.append( i )
#     return lst 
# print( lst )
#
# number = int( input( "enter :" ))
# divs = div( number )
# print( divs )


# # # 5- EKOK bulan fonksiyonu yaz. 
# def ekok_func( num1, num2 ):
    
#     i = 2 
#     ekok = 1 
    
#     while( 1 ):
        
#         if( num1 % i == 0 and num2 % i == 0 ):
#             ekok *= i
#             num1 //= i 
#             num2 //= i
        
#         elif( num1 % i != 0 and num2 % i == 0 ):
#             ekok *= i
#             num2 //= i 
                
#         elif( num1 % i == 0 and num2 % i != 0 ):
#             ekok *= i
#             num1 //= i 
        
#         else:
#             i += 1
            
#         if( num1 == 1 and num2 == 1 ):
#             break 
        
#     return ekok 

# n1 = int( input( "num1 : " ) ) 
# n2 = int( input( "num2 : " ) )  

# print( "EKOK = ", ekok_func( n1,n2 ) )


# # 5-EBOB bulan fonksiyonu yaz. 
# # VERSION 1 

# def ebob_func( num1, num2 ):
    
#     i = 2 
#     ebob = 1 
    
#     while( 1 ):
        
#         if( num1 % i == 0 and num2 % i == 0 ):
#             ebob *= i
#             num1 //= i 
#             num2 //= i
        
#         elif( num1 % i != 0 and num2 % i == 0 ):
#             num2 //= i 
                
#         elif( num1 % i == 0 and num2 % i != 0 ):
#             num1 //= i 
        
#         else:
#             i += 1
            
#         if( num1 == 1 and num2 == 1 ):
#             break 
        
#     return ebob 

# n1 = int( input( "num1 : " ) ) 
# n2 = int( input( "num2 : " ) )  

# print( "ebob = ", ebob_func( n1,n2 ) )


# # # VERSION 2 
# def ebob_func( num1, num2 ):
    
#     i = 2 
#     ebob = 1 
#     size = min( num1 ,num2)
    
#     for i in range( 2, size+1 ):
#         if ( num1 % i == 0 and num2 % i == 0 ):
#             ebob = i 

#     return ebob 

# n1 = int( input( "num1 : " ) ) 
# n2 = int( input( "num2 : " ) )  

# print( "ebob = ", ebob_func( n1,n2 ) )


# # # 5- Sayı okunuş
# birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
# onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

# def sayi_oku( sayi ):
#     ilk = sayi % 10 
#     iki = sayi // 10
    
#     return onlar[ iki ] + " " + birler[ ilk ]  

# sayi = int(input("Sayı:"))
# print( sayi_oku( sayi ) )

# # # # 6- 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanlarını bulan fonksiyon yazın.(a <= 100,b <= 100)
def ps( ):
    
    lst = list()    
    
    for i in range( 1, 101 ):
        for j in range( 1, 101 ):
            k = ( i ** 2 + j ** 2 ) ** 0.5
            if ( int( k ) == k ) :
                lst.append( (i, j, int(k) ))

    return lst

for i in ps():
    print( i )

 