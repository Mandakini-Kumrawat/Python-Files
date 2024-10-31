# Chapter - 7 Practice Set 
# Loops In Python 

# 1. Write A Program To Print Multiplication Table Of A Given Number Using Loop. 
# num = int ( input ( " Enter number : " ) ) 
# for i in range ( 1 , 11 ) :
#     print ( f" { i } = { num * i } " )

# 2. Write A Program To Greet All The Person Names Stored In A List "l" And Which Starts With S.
# l = { "Mandakini" , "MK" , "VMK" , "Vinay" , "Kabir" }
# l = { "Mandakini" , "MK" , "VMK" , "Vinay" , "Kabir" } 
# for i in l : print ( f" Hello ! , Good Morning { i } " ) 

# 3. Attempt Problem 1. Using Wwhile Loop.
# num = int ( input ( " Enter A Number :  " ) ) 
# i = 1
# while ( i < 11 ) : 
#     print ( f" { i } = { num * i } " ) 
#     i += 1

# 4. Write A Program To Find Whether A Number Is Prime Or Not.
# n = int ( input ( " Enter A Number : " ) )
# for i in range ( 2 , n ) : 
#     if ( n % i == 0 ) :
#         print ( " Not Prime ! " )
#         break 
# else : print ( " Prime ! " ) 

# 5. Write A Program To The Sum Of First N Natural Numbers Using While Loop.
# n = int ( input ( " Enter Number : " ) )
# sum = 0 
# i = 0 
# while ( i <= n ) : 
#     sum += i 
#     i += 1 
# else : print ( "Answer : " , sum ) 

# 6. Write A Program To Calculate The Factorial Of A Given Number Using The Loop. 4 : 32 
# num = int ( input ( " Enter A Number : " ) )
# sum = 1 
# for i in range ( 1 , num + 1 ) :
#     sum = sum * i 
# print ( " Answer : " , sum ) 

# 7. Write A Program To Print The Following Star Pattern. 
#          *
#        * * *
#      * * * * *        for n = 3. 
# n = int ( input ( " Enter A  Number : " ) )
# for i in range ( 0 , n ) :
#     print ( "   " * ( n - i - 1 ) , end = "") 
#     print ( " * " * ( i * 2 + 1 ) , end = "")
#     print ( " " )  

# 8. Write A Program To Print The Following Star Pattern. 
#  *
#  * *
#  * * *     for n = 3. 
# n = int ( input ( " Enter A Number : " ) )
# for i in range ( 0 , n ) :
#     print ( " * " * ( i + 1 ) , end = " " ) 
#     print ( " " ) 

# 9. Write A Program To Print The Following Star Pattern. 
#    * * *
#    *   *
#    * * *       for n = 3
# n = int ( input ( " Enter A Number : " ) ) 
# for i in range ( 0 , n ) :
#     if ( i == 0 or i == n - 1 ) :
#         print ( " * " * ( n ) , end = " " ) 
#     else : 
#         print ( " * " , end = "" ) 
#         print ( "   " * ( n - 2 ) , end = "" ) 
#         print ( " * " , end = "" )  
#     print ( " " )

# 10. Write A Proram To Print Multiplication Table Of n Using For Loop In Reversed Order. 
# n = int ( input ( " Enter A Number : " ) )
# for i in range ( 10 , 0 , -1 ) :
#     print ( f" { i } X { n } = { i * n } " )  