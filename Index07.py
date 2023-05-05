def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if len(s) <= n:
        return False
    else:
      
       return s[n]
   
v = main('uz',3)
print(v)