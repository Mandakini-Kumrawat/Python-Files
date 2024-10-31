# Chapter - 8 Practice Set
# Functions & Recursions

# 1. Write A program Using Functions To Find Greatest Of Three Numbers.
# def Greatest_Number ( a , b , c ) :
#     if ( a > b and a > c ) :
#         return a 
#     elif ( b > a and b > c ) :
#         return b 
#     else : return c  
# a = int ( input ( " Enter First Number : " ) ) 
# b = int ( input ( " Enter Second Number : " ) )
# c = int ( input ( " Enter Third number : " ) ) 
# print ( " Answer : " , Greatest_Number ( a , b , c ) )   

# 2. Write A Python Program Using Functions To Convert Celsius To Fahrenheit.
# def Celsius_To_Fahrenheit ( num ) :
#     return num * ( 9 / 5 ) + 32  
# num = int ( input ( " Enter Celsius : " ) )
# print ( " Answer : " , Celsius_To_Fahrenheit ( num ) ) 

# 3. How Do You Prevent A Python Print () Function To Print A New Line At The End. 
# print ( " By Using end ="" " , end = "" ) 

# 4. Write A Recursive Function To Calculate The Sum Of First n Natural Numbers.
# def Sum_Of_Natural_Numbers ( n , sum ) :
#     if ( n == 1 ) : return 1 
#     return n + Sum_Of_Natural_Numbers ( n - 1 , sum )
# n = int ( input ( " Enter Number : " ) ) 
# print ( " Answer : " , Sum_Of_Natural_Numbers ( n , 0 ) ) 

# 5. Write A Python Function To Print n Lines Of The Following Pattern :
#   * * *
#   * *
#   *                    for n = 3. 
# def Pattern ( n ) :
#     if ( n == 0 ) : return
#     print ( " * " * ( n ) ) 
#     return Pattern ( n - 1 )
# n = int ( input ( " Enter A Number : " ) ) 
# Pattern ( n ) 

# 6. Write A Python Function Which Converts Inches To CMs. 
# def Inches_To_Centimeter ( num ) :
#     return num * 2.54 
# num = int ( input ( " Enter A Nuber : " ) ) 
# print ( " Answer : " , Inches_To_Centimeter ( num ) )  

# 7. Write A Python Function To Remove A Given Word From A List And Strip It At The Same Time.
# def List_And_Strip ( word , l ) :
#     n = [] 
#     for item in l :
#         if not ( item == word ) :
#             n.append ( item.strip ( word ) )  
#     return n
# l = [ "MK" , "VMK" , "Vinay" , "Mandakini" , "Kabir" , "Kumrawat" ] 
# print ( " Before : " , l )
# word = input ( " Enter Word : " ) 
# print ( " After : " , List_And_Strip ( word , l ) ) 

# 8. Write A Python Function To Print Multiplication Table Of A Given Number. 
# def Multiplication_Table ( n ) :
#     for i in range ( 1 , 11 ) :
#         print ( f" { i } * { n } = { i * n } " )
# n = int ( input ( " Enter A Number : " ) )
# Multiplication_Table ( n ) 