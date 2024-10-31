# Chapter 6 - Practice Set
# Conditional Expressions

# 1. Write A Program To Find The Greatest Of Four Numberes Entered By The User. 
# a = int ( input ( " First Number : " ) ) # 1
# b = int ( input ( " Second Number : " ) ) # 4
# c = int ( input ( " Third Number : " ) ) # 2
# d = int ( input ( " Fourth Number : " ) ) # 3
# if ( a > b ) : # 5 > 2
#     if ( a > c ) : # 5 > 4 
#         if ( a > d ) : # 5 > 7 
#             print ( " Answer : " , a ) 
#         else :
#             print ( " Answer : " , d ) 
#     else :
#         if ( c > d ) :
#             print ( " Answer : " , c ) 
#         else :
#             print ( " Answer : " , d ) 
# else :
#     if ( b > c ) : # 4 > 2
#         if ( b > d ) : # 4 > 3 
#             print ( " Answer : " , b )
#         else :
#             print ( " Answer : " , d )
#     else : 
#         if ( c > d ) :
#             print ( " Answer : " , c )
#         else :
#             print ( " Answer : " , d ) 

# 2. Write A Program To Find Whether A Student Pass Or Fail If It Requires a Total of 40% and at least 33 In Each
# Subject To Pass. Assume 3 Subjects Aand Take Marks As An Input From The User. 
# m1 = int ( input ( " Marks 1 : " ) )
# m2 = int ( input ( " Marks 2 : " ) ) 
# m3 = int ( input ( " Marks 3 : " ) )
# p = ( m1 + m2 + m3 ) / 3 
# print ( " Percentage : " , p ) 
# if ( p >= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33 ) :
#     print ( " Result : Pass " )  
# else : 
#     print ( " Result : Fail " ) # 3 : 42

# 3. A Spam Comment Is Defined As Text Containing Following Keywords : " Make A lot Of Money " , " Buy Now " , 
# " Subscribe This " , " Click This ". Write A Program To Detect These Spams. 
# p1 = "Make A lot Of Money" 
# p2 = "Buy Now" 
# p3 = "Subscribe This" 
# p4 = "Click This"
# message = input ( " Enter Your Message : " )
# if ( p1 in message or p2 in message or p3 in message or p4 in message ) :
#     print ( " Spam Detected ! " , message )
# else : 
#     print ( " Message : " , message )

# 4. Write A Program To Find Whether A Given User Name Contains Less Than 10 Characters Or Not. 
# name = input ( " Enter Name : " ) 
# if ( len ( name ) < 10 ) :
#     print ( " Valid name : " , name ) 
# else : print ( " Unvalid Name : " , name ) 

# 5. Write A Program To Which Finds Out Whether A Giver Name Is Present In A String Or Not. 
# l = [ "Mandakini" , "MK" , "VMK" , "Vinay" , "Kabir" ] 
# name = input ( " Enter Your Name : " ) 
# if ( name in l ) : print ( " Yes ! " ) 
# else : print ( " No ! " ) 

# 6. Write A Program To Calculate The Grade Of A Student From His Marks From The Following Scheme : 
# 90 -> 100 => Ex 
# 80 -> 90 => A
# 70 - 80 => B
# 60 - 70 => C 
# 50 - 60 => D 
# < 50 => E
# marks = int ( input ( " Enter Yor Marks : " ) )
# if ( marks >= 90 and marks <= 100 ) : print ( " Grade : Excellent , " , marks )
# elif ( marks >= 80 and marks < 90 ) : print ( " Grade : A , " , marks ) 
# elif ( marks >= 70 and marks < 80 ) : print ( " Grade : B , " , marks ) 
# elif ( marks >= 60 and marks < 70 ) : print ( " Grade : C , " , marks ) 
# elif ( marks >= 50 and marks < 60 ) : print ( " Grade : D , " , marks ) 
# elif ( marks < 50 ) : print ( " Grade : E , " , marks ) 
# else : print ( " Invalid Marks ! " ) 

# 7. Write A Program To Find Out Whether A Given Post Is Talking About Mandakini. 
# post = "Hey , Mandakini. 4 September Was A Good Day." 
# if ( "Mandakini" in post ) : print ( " Yes ! , The Post Is About Manakini" ) 
# else : print ( " No ! , The Post Is Not About Mmandakini" ) 