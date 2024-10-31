# Chapter - 9 Practice Set
# File I/O 

# import random 

# 1. Write A Program To Read The Text From A Given PyPoem.text And Find Out Whether It Contains A Word "Twinkle".
# f = open ( "PyPoem.txt" ) 
# content = f.read () 
# if ( "Twinkle" in content ) :
#     print ( " Yes ! , Foud It. " ) 
# else : 
#     print ( " No ! , Not Found. " ) 
# f.close () 

# 2. The game() Function In A Program Lets A User Play A Game And Returns The Score As An Integer. You Need To Read A
# File "Hi-Score.text". Which Is Either Blank Or Contains The Previous Hi-Score. You Need To Write A Program To Update
# The Hi-Score Whenever The game() Function Breaks The Hi-Score. 
# def game () :
#     print ( " Game Started : " ) 
#     score = random.randint (1 , 100)
#     f = open ( "Hi-Score.txt" ) 
#     hiscore = f.read () 
#     if ( hiscore != "" ) :
#         hiscore = int ( hiscore )
#         f.close () 
#     else :
#         hiscore = 0 
#         f.close ()
#     print ( f" Your Score { score } " ) 
#     f = open ( "Hi-Score.txt" , "w" )
#     if ( score > hiscore ) : 
#         f.write ( str ( score ) ) 
#         f.close () 
#     return score 
# game () 

# 3. Write A Program To Generate Multiplicatino Tabbles From 2 to 20 And Write It To The Different Files. Place These
# Files In A Folder For A 13 - Year Old. 
# def Generate_Table ( n ) :
#     table = ""
#     for i in range ( 1 , 11 ) :
#         table += f" { n } X { i } = { n * i } \n " 
#     with open ( f"Multiplication Tables/Table_({ n }).txt" , "w" ) as f :
#         f.write ( table )


# for i in range ( 2 , 21 ) :
#     Generate_Table ( i ) 

# 4. A File Contains A Word "Donkey" Multiple Times. Yyou Need To Write A program Which Replace This Word With ######
# By Updating The Same File. 
# word = "Donkey"
# with open ( "Donkey.txt" , "r" ) as f :
#     content = f.read ()
# contentNew = content.replace ( word , "######" ) 

# with open ( "Donkey.txt" , "w" ) as f :
#     f.write ( contentNew )                            # 6 : 30 

# 5. Repeat Program 4 For A List Of Such Words. 
# words = [ "Donkey" , "Humans" , "Animals" ] 
# f = open ( "Donkey.txt" )
# content = f.read () 
# f.close () 
# for word in words :
#     Content = content.replace ( word , "#" * len ( word )  )
#     f = open ( "Donkey.txt" , "w" ) 
#     f.write ( Content ) 
#     f.close ()

# 6. Write A Program To Mine A Log File And Find Out Whether It Contains "Python".
# f = open ( "Log.html" , "r" ) 
# content = f.read ()
# if ( "Python" in content ) : print ( " Yes ! " ) 
# else : print ( " No ! " ) 
# f.close () 

# 7. Write A Program To Find Out The Line Number Where Python Is Present From Ques 6. 
# lineno = 1 
# f = open ( "Log.html" , "r" ) 
# lines = f.readlines ()
# for line in lines :
#     if ( "Python" in line ) : 
#         print ( f" Yes ! line no. { lineno } " ) 
#         break 
#     lineno += 1  
# else : 
#     f.close ()
#     print ( " No ! " ) 

# 8. Write A Program To Make A Copy Of A Text File "Donkey.txt".
# f = open ( "Donkey.txt" ) 
# content = f.read () 
# f.close ()
# f = open ( "Donkey_Copy.txt" , "w" ) 
# f.write ( content ) 
# f.close ()

# 9. Write A Program To Find Out Whether A File Is Identical & Matches The Content Of Another File. 
# f = open ( "Donkey.txt" ) 
# content1 = f.read () 
# f.close () 
# f = open ( "Donkey_Copy.txt" ) 
# content2 = f.read () 
# f.close () 
# if ( content1 == content2 ) : print ( " Yes ! " ) 
# else : print ( " No ! " ) 

# 10. Write A Program To Wipe Out The Content Of A File Using Python.  
# f = open ( "Hi-Score.txt" , "w" ) 
# f.write ( "" ) 
# f.close () 

# 11. Write A Python Program To Rename A File To "Renamed_By_Python.txt". 
# f = open ( "PyPoem.txt" ) 
# content = f.read () 
# f.close () 
# f = open ( "PyPoem_Renamed_By_Python.txt" , "w" ) 
# f.write ( content ) 
# f.close ()
    


