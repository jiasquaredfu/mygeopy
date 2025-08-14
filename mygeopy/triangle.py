import numbers
def hypot(a: float,b: float):
    '''
    Function: calculate hypotenuse of a 3-4-5 right triangle
    Args: 
        a(float): one triangle length
        b(float): second triangle length
    Output: 
        c(float): hypotenuse length

    ex: hypot(3,4) == 5
    '''
    if not (isinstance(a, numbers.Real) and isinstance(b, numbers.Real)):
        raise TypeError("a and b must be real")

    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive")
    return (a**2 + b**2) ** 0.5
