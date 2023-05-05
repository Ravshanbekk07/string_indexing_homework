def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """ 
    dig = 0
    for i in s.isnumeric():
        if int(s[i]):
            dig+=1

    return dig

v = main('32x3z')
print(v)
