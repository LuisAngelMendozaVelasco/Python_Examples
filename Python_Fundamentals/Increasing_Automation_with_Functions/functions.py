def isequaltol_vec(x, y, tol):
    maxdiff = max(abs(x - y))
    iseq = (maxdiff < tol)

    return iseq, maxdiff