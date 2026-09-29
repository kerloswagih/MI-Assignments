import utils

def palindrome_check(string: str) -> bool:
   
    ''' 
    first i convert the text to lowercase so uppercase and lowercase letters is treated the same
     then i remove all the spaces from the string so that spaces as the instructions say that 
     they must be igonred then i compared the cleaned string to its reverse and it they are 
     the same then it is a palindrome and return True otherwise return False
     
    '''
   
    normalized_string: str = string.lower().replace(" ", "")

    return normalized_string == normalized_string[::-1]

