def isnumeric(text:str) -> bool:
    
    if not text: return False
    
    if text.isdecimal(): return True
    
    if text.count('.') == 1:
        
        a,b = text.split('.')
        
        adec, bdec = a.isdecimal() or not a, b.isdecimal() or not b # checks for -> a.b <- 

        #If both a & b False means there something else we dont want... something like letters😨
        if not a and not b: 
            return False
        
        return adec and bdec #both true means it is a floating point value
    
    return False