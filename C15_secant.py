import math
import numpy as np

def secant(f, x0, x1, tol):
    """
    Secant Method

    x_{i+1} = (x_i−f(x_i)(x_i−x_{i−1})) / (f(x_i)−f(x_{i−1}))

    Input:
    - f : the equation f
    - x0,x1 : init guessing
    - tol : tolerance

    Output:
    - x1 : the approximate root
    """
    max_iter = 1000
    iter_cnt = 0

    while (np.abs(x0-x1) > tol) and (iter_cnt < max_iter):
        x0, x1 - x1, (x1 - f(x1)*(x1- x0)) / (f(x1) - f(x0))
        iter_cnt += 1

    return x1

def FalsePosition(f, a, b, steps):
    """
    False Position method

    c = (bf(a) - af(b)) / (f(a) - f(b))

    Input:
    - f : equation f
    - a,b : the range of interval
    - steps : iteration turns

    Output:
    - c : the approximate root
    """
    if (f(a) < 0) == (f(b) < 0):
        raise Exception('Incorrect interval!')

    for i in range(steps):
        fa, fb = f(a), f(b)
        c = (b*fa - a*fb) / (fa - fb)
        fc = f(c)

        if (fc < 0) == (fa < 0):
            a = c
        else:
            b = c

    return c

def IQI(f, x0, x1, x2, tol):
    """
    Inverse Quadratic Interpolation

    Input:
    - f : equation f
    - x0,x1,x2 : init guesses
    - tol : tolerance

    Output:
    - x0 : the approximate root
    """
    max_iter = 1000
    iter_cnt = 0

    while (np.abs(x0-x1) > tol) and (iter_cnt < max_iter):
        q,r,s = f(x0)/f(x1), f(x2)/f(x1), f(x2)/f(x0)
        xnew = x2 - (r*(r-q)*(x2-x1) + (1-r)*s*(x2-x0)) / ((q-1)*(r-1)*(s-1))

        x0, x1, x2 = xnew, x0, x1
        iter_cnt += 1

    return x0

def brent(f, x0, x1, tol):
    """
    Brent's Method. Also can be called by scipy.optimize.brent

    Input:
    - f : the equation f
    - x0,x1 : init guessing
    - tol : tolerance

    Output:
    - x1 : the approximate root
    """
    # init
    fx0 = f(x0)
    fx1 = f(x1)
 
    if (fx0 < 0) == (fx1 < 0):
        raise ValueError('Incorrect interval!')
 
    if abs(fx0) < abs(fx1):
        x0, x1 = x1, x0
        fx0, fx1 = fx1, fx0
 
    x2, fx2 = x0, fx0
 
    mflag = True
    max_iter = 1000
    iter_cnt = 0
 
    while (abs(x1-x0) > tol) and (iter_cnt < max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)
 
        if fx0 != fx2 and fx1 != fx2:
            q,r,s = fx0/fx1, fx2/fx1, fx2/fx0
            new = x2 - (r*(r-q)*(x2-x1) + (1-r)*s*(x2-x0)) / ((q-1)*(r-1)*(s-1))
 
        else:
            new = x1 - ( (fx1 * (x1 - x0)) / (fx1 - fx0) )
 
        if ((new < ((3 * x0 + x1) / 4) or new > x1) or
            (mflag == True and (abs(new - x1)) >= (abs(x1 - x2) / 2)) or
            (mflag == False and (abs(new - x1)) >= (abs(x2 - d) / 2)) or
            (mflag == True and (abs(x1 - x2)) < tol) or
            (mflag == False and (abs(x2 - d)) < tol)):
            new = (x0 + x1) / 2
            mflag = True
 
        else:
            mflag = False
 
        fnew = f(new)
        d, x2 = x2, x1
 
        if (fx0 * fnew) < 0:
            x1 = new
        else:
            x0 = new
 
        if abs(fx0) < abs(fx1):
            x0, x1 = x1, x0
 
        iter_cnt += 1
 
    return x1