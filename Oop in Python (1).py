# Chapter - 10 Practice Set 
# Object Oriented Programming 

from random import randint 

# 1. Creat A Class "Programmer" For Storing Information Of Few Programmers Working At Microsoft. 
# class Programmer :
#     company = "Microsoft" 
#     def __init__( self , name , salary , country ) :
#         self.name = name 
#         self.salary = salary 
#         self.country = country 

# p = Programmer ( " Mandakini " , 1000000 , "India" )
# q = Programmer ( " Vinay " , 1000000 , "India" )
# print ( p.company , p.name , p.salary , p.country ) 
# print ( q.company , q.name , q.salary , q.country ) 

# 2. Write A Class " Calculater " Capable Of Finding Square , Cube And Square Root Of A Number. 
# class Calculater :
#     def __init__( self , n ) : 
#         self.n = n 
#     def square ( self ) :
#         print ( f" Square = { self.n * self.n } " ) 
#     def cube ( self ) :
#         print ( f" Cube = { self.n * self.n * self.n } " ) 
#     def squareroot ( self ) :
#         print ( f" Square Root = { self.n ** 1 / 2 } " ) 
# a = Calculater ( 4 ) 
# a.square ()
# a.cube () 
# a.squareroot () 

# 3. Create A Class with A Class Attribute a ; Create An Object From It And Set 'a' Directly using Object.a = 0. Does
# This Change The Class Attribute. Ans = No.             # 7 : 12 
# class Demo () :
#     a = 4
# o = Demo () 
# print ( " Before : " , o.a ) 
# o.a = 0
# print ( " After : " , o.a ) 
# print ( " Demo Class Attribute Did'nt Change : " , Demo.a ) 

# 4. Add A Static Methos In Problem 2 , To Greet The User With Hello. 
# class Calculater : 
#     @staticmethod
#     def greet () :
#         print ( " Hello ! " ) 
#     def __init__( self , n ) : 
#         self.n = n
#     def square ( self ) :
#         print ( f" Sqare : { self.n * self.n } " )
#     def cube ( self ) :
#         print ( f" Cube : { self.n * self.n * self.n } " ) 
#     def squareroot ( self ) :
#         print ( f" Square Root : { self.n ** 1 / 2 } " )
# a = Calculater ( 4 )
# a.greet () 
# a.square () 
# a.cube () 
# a.squareroot ()

# 5. Write A Class Train Which Has Methods To Book A Ticket , Get Status ( No. Of Seats ) and Get The Fare Information
# Of Train Running Under Indian Railways. 
# class Train :
#     def __init__(self , trainNo ) :
#         self.trainNo = trainNo  
#     def book_tickets ( self , fro , to) :
#         print ( f" Ticket Is Booked For Tain No. { self.trainNo } From { fro } To { to } " ) 
#     def get_status ( self ) : 
#         print ( f" Tain No. { self.trainNo } : Train Is Running On Time. " ) 
#     def get_fare ( self , fro , to ) :
#         print ( f" The Fare For Tain No. { self.trainNo } From { fro } To { to } is { randint ( 222 , 5555 ) } " )  
# t = Train ( 345 ) 
# t.book_tickets ( "Khargone" , "Mumbai" ) 
# t.get_status () 
# t.get_fare ( "Khargone" , "Mumbai" ) 

# 6. Can You Change The Self-Parameter Inside A Class To Something Else ( Say "Mandakini" ). Try Changing Self To "slf"
# Or "Mandakini" Aand See The Effects.
# class Programmer :
#     company = "Microsoft" 
#     def __init__( slf , name , salary , country ) :
#         slf.name = name 
#         slf.salary = salary 
#         slf.country = country 

# p = Programmer ( " Mandakini " , 1000000 , "India" )
# q = Programmer ( " Vinay " , 1000000 , "India" )
# print ( p.company , p.name , p.salary , p.country ) 
# print ( q.company , q.name , q.salary , q.country )  