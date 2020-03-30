import numpy as np
from scipy.misc import derivative
import math

def newton(func, x0, tol=1e-6):
    '''
    Newton method

    x_{i+1} = x_i - f(x_i)/df(x_i)

    Input:
    - func : equation f
    - x0 : init point
    - tol : tolerance

    Output:
    - x : the approximate root
    '''
    x = x0
    while np.abs(func(x) - 0) >= tol:
        df = derivative(func, x, dx=1e-6)
        x -= func(x)/df
    return x

def modified_newton(func, x0, m, steps=None):
    """
    Modified Newton method when containing a root of r of multiplicity of m>1

    x_{i+1} = x_i - mf(x_i)/df(x_i)

    Input:
    - func : equation f
    - x0 : init point
    - m : multiplicity
    - steps : steps of iteration

    Output:
    - x : the approximate root
    """
    if steps is None:
        steps = math.ceil(math.log(0.5e-6, (m-1)/m))
    x = x0
    for i in range(steps):
        df = derivative(func, x, dx=1e-6)
        x -= m*func(x)/df
    return x

def newton_digits(func, x0, n=8):
    """
    Newton method find the root 

    Input:
    - func : target function
    - x0 : init value
    - n : required decimals

    Output:
    - x : approximate solution
    """
    count_iter = 1
    max_iter = 10000

    while (np.abs(func(x0)/derivative(func, x0, dx=1e-6)) > 0.5*10**(-n)) and (count_iter < max_iter):
        x0 = x0-func(x0)/derivative(func, x0, dx=1e-6)
        count_iter += 1

    return round(x0, n)

def show_errors(func, x0, root, m):
    xc = modified_newton(func, x0, m)
    FE = np.abs(xc-root)
    BE = np.abs(func(xc))
    print('The approximate root is:', xc, 'forward error is:', FE, 'backward error is:', BE)


if __name__ == '__main__':
    f = lambda x:3*x**2-100*np.log2(x)
    print(newton(f, 10))
    '''
    test1 = lambda x:x**3+x-1
    print('The root of test1 is:', newton(test1, -0.7))
    test2 = lambda x:np.sin(x)+x**2*np.cos(x)-x**2-x
    print('The root of test2 is:', newton(test2, 1, 1e-10))
    print('Use modified newton test2 root is:', modified_newton(test2, 1, m=3))
    print('The root of 6 decimals of test2 is:', newton_digits(test2, 1, n=6))
    # problem 1
    print('='*30)
    print('Problem 1.4-1')
    f1a = lambda x:x**3-2*x-2
    print('(a):', newton_digits(f1a, 2, n=8))
    f1b = lambda x:np.exp(x)+x-7
    print('(b):', newton_digits(f1b, 1, n=8))
    f1c = lambda x:np.exp(x)+np.sin(x)-4
    print('(c):', newton_digits(f1c, 1, n=8))
    # problem 2
    print('='*30)
    print('Problem 1.4-2')
    f2a = lambda x:x**5+x-1
    print('(a):', newton_digits(f2a, 0))
    f2b = lambda x:np.sin(x)-6*x-5
    print('(b):', newton_digits(f2b, -1))
    f2c = lambda x:math.log(x)+x**2-3
    print('(c):', newton_digits(f2c, 1))
    # problem 3
    print('='*30)
    print('Problem 1.4-3')
    f3a = lambda x:27*x**3+54*x**2+36*x+8
    # (a) root: -2/3 multiplicity of 3
    print('(a):')
    show_errors(f3a, -1, -2/3, 3)
    # (b) root: 1/6 multiplicity of 2
    f3b = lambda x:36*x**4-12*x**3+37*x**2-12*x+1
    print('(b):')
    show_errors(f3b, 0, 1/6, 2)
    # problem 4
    print('='*30)
    print('Problem 1.4-4')
    f4a = lambda x:2*np.exp(x-1)-x**2-1
    # (a) root: 1 multiplicity of 3
    print('(a):')
    show_errors(f4a, 0, 1, 3)
    f4b = lambda x:math.log(3-x)+x-2
    # (b) root: 2 multiplicity of 2
    print('(b):')
    show_errors(f4b, 1, 2, 2)
    # problem 5
    print('='*30)
    print('Problem 1.4-5')
    # f(x) = 2/3 * pi * r**3 + 10*pi*r**2 - 400
    f5 = lambda x:2/3*math.pi*x**3 + 10*math.pi*x**2 - 400
    print('The radius of the well is:', newton_digits(f5, 5, 4))
    # problem 6
    print('='*30)
    print('Problem 1.4-6')
    # f(x) = 2/3*pi*r**3 + 1/3*pi*r**2*10 - 60
    f6 = lambda r:2/4*math.pi*r**3 + 1/3*10*math.pi*r**2 - 60
    print('The radius of the ice-cream is:', newton_digits(f6, 5, 4))'''