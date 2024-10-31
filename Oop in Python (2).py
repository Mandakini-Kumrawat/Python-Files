# Chapter - 11 Practice Set 
# Inheritance

# 1. Create A Class ( 2 - D vector ) And Use It To Create Another Class Representing A 3-D Vector.
# class Two_D_Vector :
#     def __init__( self , i , j ) :
#         self.i = i
#         self.j = j
#     def show ( self ) :
#         print ( f" The Vector Is { self.i } i + { self.j } j " )
# class Three_D_Vector ( Two_D_Vector ) :
#     def __init__( self , i , j , k ) :
#         super().__init__( i , j )
#         self.k = k
#     def show(self):
#         print( f" The Vector Is { self.i } i + { self.j } j + { self.k } k " )
# a = Two_D_Vector ( 1 , 2 )
# a.show ()
# b = Three_D_Vector ( 1 , 2 , 3 )
# b.show ()

# 2. Create A Class "Pets" From A Class "Animals" And Further Create A Class "Dog" From "Pets". Add A Method "Bark" To
# Class "Dog".                          # 7 : 51
# class Animals :
#     pass
# class Pets ( Animals ) :
#     pass
# class Dog ( Pets ) :
#     @staticmethod
#     def bark () :
#         print ( " Bow Bow ! " )
# d = Dog ()
# d.bark ()

# 3. Create A Class 'Employee' And Add Salary And Increment Properties To It.
# Write A Method 'SalaryAfterIncrement' Method With A @property decorator With A Setter Which Changes The Value Of
# Increment Based On The Salary.
# class Employee :
#     Salary = 250
#     Increment = 20
#     @property
#     def Salary_After_Increment ( self ) :
#         return self.Salary + ( self.Salary * self.Increment ) / 100
#     def Set_Salary ( self , Salary ) :
#         self.Increment = ( ( Salary / self.Salary ) -1 ) * 100
# e = Employee ()
# print ( f" Salary : { e.Salary } , \n Increment : { e.Increment } % " )
# print ( f" Total Salary Increment : { e.Salary_After_Increment } " )
# print ( f" Total Salary Increment : { e.Set_Salary } " )

# 4. Write A Class 'Complex' To Represent Complex Numbers , Along With Overloaded Operators With '+' And '*'. Which Adds
# And Multiply Them.               # 7 : 59
# class complex :
#     def __init__ ( self , r , i ) :
#         self.r = r
#         self.i = i
#     def __add__ ( self , c2 ) :
#         return complex ( self.r + c2.r , self.i + c2.i )
#     def __str__ ( self ) :
#         return f" { self.r } + { self.i } i "
# c1 = complex ( 1 , 3 )
# c2 = complex ( 2 , 3 )
# print ( c1 + c2 )

# 5. Write A Class Vector Representing A Vector Of n Dimensions. Overload The + And * Operator Which Calculates The Sum
# And The Dot (.) Product Of Them.
# class vector :
#     def __init__ ( self , x , y , z ) :
#         self.x = x
#         self.y = y
#         self.z = z
#     def __add__( self , other ) :
#         result = ( self.x + other.x , self.y + other.y , self.z + other.z )
#         return result
#     def __mul__ ( self , other ) :
#         result = ( self.x * other.x + self.y * other.y + self.z * other.z )
#         return result
#     def __str__( self ) :
#         return f" ( vector { self.x } , { self.y } , { self.z } ) "
# v1 = vector ( 1 , 3 , 5 )
# v2 = vector ( 2 , 3 , 1 )
# v3 = vector ( 7 , 4 , 1 )
# print ( " V1 + V2 = " , v1 + v2 )
# print ( " V1 * V2 = " , v1 * v2 )
# print ( " V2 + V3 " , v2 + v3 )
# print ( " V2 * V3 " , v2 * v3 )
# print ( " V1 + V3 " , v1 + v3 )
# print ( " V1 * V3 " , v1 * v3 )

# 6. Write __str__() Method To Print The Vector As Follows :
#    7i  +  8j  +  10k  , Assume Vector Of 3 For This Problem.
# class Vector :
#     def __init__ ( self , x , y , z ) :
#         self.i = x
#         self.j = y
#         self.k = z
#     def __str__ ( self ) :
#         return f" { self.i } i + { self.j } j + { self.k } k "
# V = Vector ( 2 , 8 , 4 )
# print ( " Answer : " , V )

# 7. Override The __len__() Method On Vector Of Problem 5 To Display The Dimension Of The Vector.
# class V :
#     def __init__ ( self , list ) :
#         self.l = list
#     def __len__ ( self ) :
#         return len ( self.l )
# v = V ( [ 2 , 8 , 4 ] )
# print ( " Length Of Vector V : " , len ( v ) )

