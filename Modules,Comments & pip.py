# Chapter - 1 Practice Set 
# Modules , Comments & PIP. 

# 1. Write A Program To Print Poem In Python.
# print ( ''' Twinkle Twinkle Little Star , 
#        How I Wonder What You Are ,
#        Up Above The World So High ,
#        Like A Dimond , In tHe Sky. ''' ) 28:26

# 2. Use REPL ( Read , Evaluate , Print , Loop ) and Print The Table Of 5 Using It.
 
# 3. Install An External Module And Use It To Perform An operation Of Your Intereset. ( Module - pyttsx )
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait() 

# 4. Write A Program To Print The Contents Of A Directory Using The OS Module. Search online For The Function Which 
#    Does That.
# import os

# def print_directory_contents(directory):
#     try:
#         # Get a list of files and directories in the specified directory
#         contents = os.listdir(directory)
        
#         print(f"Contents of '{directory}':")
#         for item in contents:
#             print(item)
#     except FileNotFoundError:
#         print(f"The directory '{directory}' does not exist.")
#     except PermissionError:
#         print(f"Permission denied to access '{directory}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Specify the directory you want to print the contents of
# directory_path = '/'
# print_directory_contents(directory_path)

# 5. Label The Program Written In Problem 4 With Comments. 