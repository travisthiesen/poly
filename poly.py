def poly_diff(p):
    deg_p = len(p) - 1
    if deg_p == 0:
        return [0]
    else:
        return [k*p[k] for k in range(1,deg_p+1)]