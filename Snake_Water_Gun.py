import random
'''
  1  For  Snake
 -1  For  Water
  0  For  Gun 
'''
computer = random.choice ( [ -1 , 1 , 0 ] )  
youstr = input ( " Enter Your Choice : " ) 
youDic = { "s" : 1 , "w" : -1 , "g" : 0 } 
reverseDic = { 1 : "Snake" , -1 : "Water" , 0 : "Gun" }
you = youDic [ youstr ] 
print ( f" You : { reverseDic [ you ] } \n Computer : { reverseDic [ computer ] } " ) 
if ( computer == you ) :
    print ( " Draw ! " ) 
elif ( computer == -1 and you == 1 ) :
    print ( " You Win ! " )  
elif ( computer == -1 and you == 0 ) :
    print ( " You Lose ! " ) 
elif ( computer == 1 and you == -1 ) :
    print ( " You Lose ! " ) 
elif ( computer == 1 and you == 0 ) :
    print ( " You Win ! " ) 
elif ( computer == 0 and you == -1 ) :
    print ( " You Win ! " ) 
elif ( computer == 0 and you == 1 ) :
    print ( " You Lose ! " ) 
else : print ( " Something Went Wrong. Try Again ! " ) 