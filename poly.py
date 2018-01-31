def poly_diff(p):
    "Computes the derivative of a polynomial"
    deg_p = len(p) - 1
    # returns 0 if the inputed function is a constant
    if deg_p == 0:
        return [0]
    # returns the derivative of a polynomial with exponents > 0
    else:
        return [k*p[k] for k in range(1,deg_p+1)]
    
    
    