# Chapter - 13 Practice Set
# Advance Python 2

from functools import reduce

# 1. Create Two Virtual Environments , Install Few Packegaes In The First One. How Do You Create A Similar Environment In The
# Second One ?

# 2. Write A Program To Input Name , Marks And Phone Number Of A Student And Format It Using The Format Function Like Below.
# "The Name Of The Student Is Mandakini , Her Marks Are 88 And Phone Number Is ********27."
# name = "Mandakini"
# marks = 88
# PhoneNo = "********27"
# s = "The Name Of The Student Is {} , Her Marks Are {} And Phone Number Is {}.".format ( name , marks , PhoneNo )
# print ( s )

# 3. A List Contains The Multiplication Table Of 7. Write A Program To Convert It To Vertical String Of Same Numbers.
# table = [ str ( i * 7 ) for i in range ( 1 , 11 ) ]
# s = "\n".join ( table )
# print ( s )

# 4. Write A Program To Filter A list Of Numbers Which Are Divisible By 5.
# def divisible ( n ) :
#     if ( n % 5 == 0 ) :
#         return True
#     return False
# a = [ 2 , 6 , 5 , 20 , 45 , 11 , 10 , 32 , 55 ]
# f = list ( filter ( divisible , a ) )
# print ( f )

# 5. Write A Program To Find The Maximum Of The Numebrs In A List Using The Reduce Function.
# def maximum ( a , b ) :
#     if ( a > b ) :
#         return a
#     return b
# n = [ 2 , 6 , 5 , 20 , 45 , 11 , 10 , 32 , 55 ]
# f = list ( Reduce ( maximum , n ) )
# print ( f )

# 6. Run pip Freeze For The System Interpreter. Take The Contents And Create A Similar Virtual Environment. 