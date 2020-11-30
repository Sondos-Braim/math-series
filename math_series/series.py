def fibonacci(n): 
    if n<0: 
        return "Incorrect input"
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2) 

def lucas(n): 
    if n<0: 
        return "Incorrect input"
    # First lucas number is 0 
    elif n==0: 
        return 2
    # Second lucas number is 1 
    elif n==1: 
        return 1
    else: 
        return lucas(n-1)+lucas(n-2) 

def sum_series(n,n0=0):
    if n<0: 
        return "Incorrect input"
    # First sum_series number is 0 
    elif n==0: 
        return n0
    # Second sum_series number is 1 
    elif n==1: 
        return 1
    else: 
        return sum_series(n-1)+sum_series(n-2) 

  