# We Are Going To Write A Program That Generates A Random Number And Asks The User To Guess It.
#
# If The Player (s) Guess Is Higher Than The Actual Numebr , The Program Displays , " Lower Number Please ! ". Similarly , If
# The User (s) Guess Is Too Low , The Program Prints , " Higher Number Please ! ". When The User Guesses The Correct Number ,
# The Program Displays The Number Of Guesses The Player Used To Arrive At The Number.
#
# Hint : Use The Random Module.                #  8  :  9 

import random
n = random.randint ( 1 , 10 )
a = - 1
guesses = 0
while ( a != n ) :
    guesses += 1
    a = int ( input ( " Guess A Number : " ) )
    if ( a == n ) :
        print ( " Correct ! \n Number Of guesses : " , guesses )
        break
    elif ( a < n ) :
        print ( " Higher Number Please " )
    elif ( a > n ) :
        print ( " Lower Number Please " )


try :
    a = int ( input ( " Enter A Number : ") )
    print ( a )
except Exception as e :
    print ( " Exception : " , e )
else :
    print ( " Run Successfully ! " )        # 8 : 34

