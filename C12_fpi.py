# exercise 1.2
# use function 'fpi' to solve problems
# like f(x) = x
from math import e, log, sin, asin, cos

def fpi(f, x0, k):
    '''
    find the fixed-point of f within k iterations

    Input:
    - f : target function
    - x0 : init value
    - k : turns of iterations

    Output:
    - x : approximate solution
    '''
    x = x0

    for i in range(k):
        x = f(x)

    return x

def fpi_digits(f, x0, n):
    '''
    find the fixed-point of f within k iterations

    Input:
    - f : target function
    - x0 : init value
    - n : required decimals

    Output:
    - xc : approximate solution
    '''
    x, xc = x0, f(x0)

    current_iter = 0
    max_iter = 1000

    while (abs(x - xc) > 0.5*10**(-n)) and (current_iter < max_iter):
        x, xc = xc, f(xc)

        current_iter += 1

    if current_iter < max_iter:
        print('We find the xc in {} steps.'.format(current_iter))
    else:
        print('The algorithm doesn\'t converage within max iterations.')

    return round(xc, n)

def isConverge(df, fp):
    '''
    whether the fixed point is locally converged.

    Input:
    - df : the derivation of f
    - fp : fixed point
    '''
    S = abs(df(fp))

    print('According to theorem 1.6:')
    print('S =', S)
    if S < 1:
        print('The fixed point locally converged.')
    else:
        print('The fixed point locally unconverged.')

if __name__ == '__main__':
    print('Test result:')
    f = lambda x: (1 + 2*x**3) / (1 + 3*x**2)
    print('Point is:', fpi(f, 0.5, 10))
    print('='*30)

    x_ori = 1
    print('Problem 1.2-1')
    f1a = lambda x: (2*x + 2)**(1/3)
    print('(a):', fpi_digits(f1a, x_ori, 8))
    f1b = lambda x: log(7 - x)
    print('(b):', fpi_digits(f1b, x_ori, 8))
    f1c = lambda x: log(4 - sin(x))
    print('(c):', fpi_digits(f1c, x_ori, 8))
    print('='*30)

    x_ori = 1
    print('Problem 1.2-2')
    f2a = lambda x: (x + 1) / (x**4 + 2)
    print('(a):', fpi_digits(f2a, x_ori, 8))
    f2b = lambda x: (sin(x) - 5) / 6
    print('(b):', fpi_digits(f2b, x_ori, 8))
    f2c = lambda x: (3 - log(x))**0.5
    print('(c):', fpi_digits(f2c, x_ori, 8))
    print('='*30)

    print('Problem 1.2-3')
    x_ori = 1
    print('X0:', x_ori)
    f3a = lambda x: (x + 3/x)/2
    print('(a):', fpi_digits(f3a, x_ori, 8))
    f3b = lambda x: (x + 5/x)/2
    print('(b):', fpi_digits(f3b, x_ori, 8))
    print('='*30)

    print('Problem 1.2-4')
    x_ori = 1
    print('X0:', x_ori)
    f4a = lambda x: (2*x + 2/x**2)/3
    print('(a):', fpi_digits(f4a, x_ori, 8))
    f4b = lambda x: (2*x + 3/x**2)/3
    print('(b):', fpi_digits(f4b, x_ori, 8))
    f4c = lambda x: (2*x + 5/x**2)/3
    print('(c):', fpi_digits(f4c, x_ori, 8))
    print('='*30)

    print('Problem 1.2-5')
    x_ori = 1
    f5 = lambda x: cos(x)**2
    fp = fpi_digits(f5, x_ori, 6)
    print('Fixed Point is:', fp)
    df5 = lambda x: -sin(2*x)
    isConverge(df5, fp)
    print('='*30)