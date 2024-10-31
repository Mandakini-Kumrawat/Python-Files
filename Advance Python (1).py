# Chapter - 12 Practice Set
# Advance Python 1

# 1. Write A Program To Open Three Files 1.txt , 2.txt , 3.txt. If Any Of These Files Are Not Present , A Message Without
# Exiting The Program Must Be Printed Propting The Same.
# try :
#     with open ( "text_1.txt" ) as f :
#         content = f.read ()
#         print ( content )
# except Exception as e :
#     print ( " File Not Found ! " , e )
#
# try :
#     with open ( "Donkey.txt" ) as f :
#         content = f.read ()
#         print ( content )
# except Exception as e :
#     print ( " File Not Found ! " , e )

# 2. Write A Program To Pirnt The Third , Fifth And Seventh Element From A List Using Enumerate Function.
# l = [ 22 , 13 , 45 , 62 , 25 , 11 , 32 , 74 , 36 ]
# for i , item in enumerate ( l ) :
#     if i == 2 or i == 4 or i == 6 :
#         print ( f" { i + 1 } = { item } " )

# 3. Write A list Comprehension To Print A List Which Contains The Multiplication Table Of A User Entered Number.
# n = int ( input ( " Enter A Number : " ) )
# table = [ n * i for i in range ( 1 , 11 ) ]
# print ( table )

# 4. Write A Program To Display a/b Where a And b Are Integers. if b = 0 , Display Infinite By Handling The 'ZeroDivision'
# Error.
# try :
#     a = int ( input ( " Enter a : " ) )
#     b = int ( input ( " Enter b  : " ) )
#     print(" Answer : ", a / b)
# except ZeroDivisionError as e :
#     print ( " Zero Value ! " , e )

# 5. Store The Multiplication Genrated In Problem 3 In A File Named txt. # 8  :  55
# n = int ( input ( " Enter A Number : " ) )
# table = [ n * i for i in range ( 1 , 11 ) ]
# with open("Table.txt", "a") as f:
#     f.write ( f" Table Of { n } = { str ( table ) } \n" )