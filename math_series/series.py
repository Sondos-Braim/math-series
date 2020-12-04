def fibonacci(n): 
    """
    This function takes in a number and returns a fibonacci value of it which is the sum of the fibonacci value of the two nambers before and it uses recursion.
    """
    if n<0: 
        return "Incorrect input"
    elif n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2) 

def lucas(n): 
    """
    This function takes in a number and returns a lucas value of it which is the sum of the lucas value of the two nambers before and it uses recursion.
    """
    if n<0: 
        return "Incorrect input"
    elif n==0: 
        return 2
    elif n==1: 
        return 1
    else: 
        return lucas(n-1)+lucas(n-2) 

def sum_series(n,n0=0,n1=1):
    """
    This function takes in a number and returns a fibonacci value of it which is the sum of the fibonacci value of the two nambers before and it uses recursion when two optional arguments are passed, it returns the lucas value.
    """
    if n<0: 
        return "Incorrect input"
    elif n==0: 
        return n0
    elif n==1: 
        return n1
    else: 
        return sum_series(n-1)+sum_series(n-2) 

  