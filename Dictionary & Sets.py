# Chapter - 5 Practice Set
# Dictionary & Sets. 

# . Write A Program To Create A Dictionary With Hindi Words With Values In Their English Translation. Provide User With
# An Option To Look It Up.
# dic = { "Sher" : "Lion" , "Cheeta" : "Tiger" , "Mandakini" : "River" , "Pani" : "Water" , "Ek" : "One" , "Do" : "Two" }
# n = input ( " Enter Hindi Word : " ) 
# print ( dic [ n ] ) 

# . Write A Program To Input Eight Numbers From The User And Display All The Unique Numbers ( Once ).
# s = set () 
# n = int ( input ( " One : " ) )  
# s.add  ( n )
# n = int ( input ( " Two : " ) )  
# s.add  ( n )
# n = int ( input ( " Three : " ) )  
# s.add  ( n )
# n = int ( input ( " Four : " ) )  
# s.add  ( n )
# n5 = int ( input ( " Five : " ) )  
# s.add  ( n5 )
# n6 = int ( input ( " Six : " ) )  
# s.add  ( n6 )
# n7 = int ( input ( " Seven : " ) )  
# s.add  ( n7 )
# n8 = int ( input ( " Eight : " ) )  
# s.add  ( n8 )
# print ( s ) 

# . Can We Have 8 As Int And Str In A Set.
# s = ( 8 , "8" ) 
# print ( s ) 

# . What Will Be The Length oF The Following Set s :
# s = set () 
# s.add ( 0 ) 
# s.add ( 0.0 ) 
# s.add ( '0' ) # Length Of s After These Operations. 
# print ( len ( s ) ) 

# 5. s = {} , What Is The Type Of s ? 
# s = {}
# print ( type ( s ) )

# 6. Create An Empty Dictionary. Allow  Friends To Enter Their Language As Value And Use Key As Their Names. Assume  
# That The Names Are Unique.
# dic = {} 
# k = input ( " First Name : " ) 
# v = input ( " Fevorite Lang : " ) 
# dic.update ( { k : v } ) 
# k = input ( " Second Name : " ) 
# v = input ( " Fevorite Lang : " ) 
# dic.update ( { k : v } ) 
# k = input ( " Third Name : " ) 
# v = input ( " Fevorite Lang : " ) 
# dic.update ( { k : v } ) 
# k = input ( " Fourth Name : " ) 
# v = input ( " Fevorite Lang : " ) 
# dic.update ( { k : v } ) 
# print ( dic ) 

# 7. Can You Change The Values Inside A List Which Is Contained In A Set s. 
# s = { 8 , 7 , 12 , "MK" , [ 1 , 2 ] } 
# Answer : List Can Not Be Included As An Element In SET. Set are immutable. 