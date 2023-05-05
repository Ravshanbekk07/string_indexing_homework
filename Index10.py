def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a = int(s)
    x1  = a%10
    x2 = a%100//10
    x3 = a%1000//100
    x4 = a//1000%10
    x5 = a//1000//10
    return x5 +x1+x2+x3+x4


v = main('12332')
print(v)
