# exercise 1.1
# use function 'bisect' to realize 
# looking for the root of equation by bisect

from math import log2, log, e
from math import ceil, floor
from math import cos, sin 
import matplotlib.pyplot as plt
import numpy as np

def bisect(f, a, b, tol):
    '''
    calculate the approximate solution of f(x)=0

    Input:
    - f : quation f
    - a : interval lower bound
    - b : interval upper bound  f(a)*f(b)<0
    - tol : tolerance

    Output:
    - xc : approximate solution of f
    '''
    if (f(a) < 0) == (f(b) < 0):
        raise Exception('Incorrect interval!')

    fa, fb = f(a), f(b)

    while (b-a)/2 > tol:
        c = (a+b)/2
        fc = f(c)

        if fc == 0:
            return c

        if (fa < 0) == (fc < 0):
            a, fa = c, fc

        else:
            b, fb = c, fc

    return (a+b) / 2

def bisect_digits(f, a, b, p):
    '''
    calculate the approximate solution of f(x) to
    the nearest p decimal places

    Input:
    - f : quation f
    - a : interval lower bound
    - b : interval upper bound  f(a)*f(b)<0
    - p : solution to the nearest p decimal places

    Output:
    - xc : approximate solution
    '''
    if (f(a) < 0) == (f(b) < 0):
        raise Exception('Incorrect interval!')

    n = ceil(log2((b-a) / (0.5 * 10**(-p))) - 1)
    print('Original Interval is [{},{}]'.format(a, b))
    print('To get {} decimal, we need {} steps.'.format(p, n))

    fa, fb = f(a), f(b)

    for i in range(n):
        c = (a+b) / 2
        fc = f(c)

        #print('Before {} loop, a={}, b={}, c={}'.format(i, a, b, c))

        if (fa < 0) == (fc < 0):
            a, fa = c, fc

        else:
            b, fb = c, fc

        #print('After this loop, a={}, b={}, c={}'.format(a, b, c))

    return round((a+b) / 2, p) 

def plot_functions(f1, f2, f3):
    x = np.linspace(0,1,1000)
    plt.subplot(311)
    plt.plot(x, f1(x))
    plt.xlim(-2,2)
    plt.ylim(-1, 1)
    plt.subplot(312)
    plt.plot(x, f2(x))
    plt.xlim(-2,2)
    plt.ylim(-1, 1)
    plt.subplot(313)
    plt.plot(x, f3(x))
    plt.xlim(-2,2)
    plt.ylim(-1, 1)

    plt.show()

    return plt

if __name__ == '__main__':
    print('Test result:')
    f1 = lambda x: x**3 + x - 1
    print(bisect(f1, 0, 1, tol=0.00005))
    print('='*30)

    print('Problem 1.1-1')
    f1a = lambda x: x**3 - 9
    print('(a):', bisect_digits(f1a, 2, 3, 6))
    f1b = lambda x: 3*x**3 + x**2 - x - 5
    print('(b):', bisect_digits(f1b, 1, 2, 6))
    f1c = lambda x: cos(x)**2 -x + 6
    print('(c):', bisect_digits(f1c, 6, 7, 6))
    print('='*30)

    print('Problem 1.1-2')
    f2a = lambda x: x**5 + x - 1
    print('(a):', bisect_digits(f2a, 0, 1, 8))
    f2b = lambda x:sin(x) -6*x -5
    print('(b):', bisect_digits(f2b, -2, 0, 8))
    f2c = lambda x: log(x) + x**2 - 3
    print('(c):', bisect_digits(f2c, 1, 10, 8))
    print('='*30)

    print('Problem 1.1-3')
    f3a = lambda x: 2*x**3 - 6*x - 1
    f3b = lambda x: e**(x-2) + x**3 - x
    f3c = lambda x: 1 + 5*x - 6*x**3 - e*(2*x)
    #plot_functions(f3a, f3b, f3c)
    print('='*30)

    ziplist = [(2, 'a'), (3, 'b'), (5, 'c')]
    print('Problem 1.1-4')
    for i, j in ziplist:
        f4 = lambda x: x**2 - i
        print(j, bisect_digits(f4, 1, 3, 8))
    print('='*30)

    print('Problem 1.1-5')
    for i, j in ziplist:
        f5 = lambda x: x**3 - i
        print(j, bisect_digits(f5, 1, 3, 8))
    print('='*30)

    print('Problem 1.1-6')
    f6 = lambda x: cos(x)-sin(x)
    print('Approximate solution is:', bisect_digits(f6, 0, 1, 6))
    print('='*30)

    print('Problem 1.1-7')
    f7 = lambda x: np.linalg.det([[1,2,3,x],[4,5,x,6],[7,x,8,9],[x,10,11,12]]) - 1000
    x1 = bisect_digits(f7, -18, -17, 6)
    det1 = f7(x1)
    acc1 = ceil(log(abs(det1*2), 10))
    print('First root is:', x1)
    print('The det is: {} with {} decimal acc.'.format(det1 + 1000, -acc1))
    x2 = bisect_digits(f7, 9, 10, 6)
    det2 = f7(x2)
    acc2 = ceil(log(abs(det2*2), 10))
    print('Second root is:', x2)
    print('The det is:', det2)
    print('The det is: {} with {} decimal acc.'.format(det2 + 1000, -acc2))
    print('='*30)

    print('Problem 1.1-8')
    hibm = 1 / (np.arange(0, 5) + np.arange(1, 6)[:,np.newaxis])
    def f8(x):
        hibm[0][0] = x
        return np.linalg.eig(hibm)[0].max() - np.pi
    print('A_11 is:', bisect_digits(f8, 2, 3, 6))
    print('='*30)

    print('Problem 1.1-9')
    # v=4/3*pi*r^3 > 1*2
    f9 = lambda x: np.pi * x**2 * (1 - 1/3 * x) - 1
    print('The height is:', bisect(f9, 0, 1, 1e-3))
    print('='*30)