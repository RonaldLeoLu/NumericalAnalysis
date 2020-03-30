from scipy import optimize
import numpy as np
from C11_bisect import bisect

def wilkpoly(x, n=20):
    return np.prod(np.array([x-i for i in range(1,n+1)]))

def problem1():
    print('Problem 1.3-1')
    f1 = lambda x:np.sin(x)-x
    xc = optimize.fsolve(f1, 0.1)[0]
    FE1 = np.abs(xc - 0)
    BE1 = np.abs(f1(xc))
    print('(b):','xc =',xc,'forward error =',FE1,'backward error =',BE1)

def problem2():
    print('Problem 1.3-2')
    f2 = lambda x:np.sin(np.power(x,3))-np.power(x,3)
    xc = optimize.fsolve(f2, 0.1)[0]
    FE2 = np.abs(xc - 0)
    BE2 = np.abs(f2(xc))
    print('(b):','xc =',xc,'forward error =',FE2,'backward error =',BE2)

def problem3():
    print('Problem 1.3-3')
    f3 = lambda x: 2*x*np.cos(x)-2*x+np.sin(np.power(x,3))
    xc = optimize.fsolve(f3, 0.1)[0]
    FE3 = np.abs(xc - 0)
    BE3 = np.abs(f3(xc))
    print('(a):','xc =',xc,'forward error =',FE3,'backward error =',BE3)
    xa = bisect(f3, -0.1, 0.2, 1e-10)
    FEb = np.abs(xa)
    BEb = np.abs(f3(xa))
    print('(b):','xc =',xa,'forward error =',FEb,'backward error =',BEb)

def problem4():
    print('Problem 1.3-4')
    f4 = lambda x:x**3-3*x**2+x-3
    g4 = lambda x:x**3
    df = lambda x:3*x**2-6*x+1
    epsilon = 1e-3
    DeltaR = -epsilon * g4(3)/df(3)
    xc = 3 + DeltaR
    print('(b) accurate root is:', xc)

def problem5():
    print('Problem 1.3-5')
    f5 = lambda x:np.prod(np.array([x-i for i in range(1,5)]))
    df = lambda x:(x-2)*(x-3)*(x-4) \
            + (x-1)*(x-3)*(x-4) \
            + (x-1)*(x-2)*(x-4) \
            + (x-1)*(x-2)*(x-3)
    g5 = lambda x:np.power(x, 6)
    epsilon = -1e-6
    DeltaR = -epsilon*g5(4)/df(4)
    xc = 4 + DeltaR
    # error magnification factor
    emf = np.abs(g5(4)/(4*df(4)))
    f = lambda x:np.prod(np.array([x-i for i in range(1,5)])) \
            - 1e-6 * np.power(x, 6)
    xa = optimize.fsolve(f, 4)[0]
    print('The sensitivity root is:',xc,'The fzero root is:',xa,'Error magnification factor:',emf)

def problem6():
    print('Problem 1.3-6')
    print('The accurate root is:', optimize.fsolve(wilkpoly, 15)[0])

if __name__ == '__main__':
    print('First print some examples in the textbook.')
    # Here we can use scipy.optimize.fsolve instead of fzero.m
    # They are totally called in the same way. 
    f = lambda x:x**3-2*x**2+4/3*x-8/27
    print('The root of the test equation is:',optimize.fsolve(f, 1)[0])
    # Here we use 'numpy' to realize the wilk poly 
    # in its factored form so we have an accurate solution.
    print('The root of wilkinson poly is:', optimize.fsolve(wilkpoly, 16)[0])
    # Problems
    problem1()
    print('='*30)
    problem2()
    print('='*30)
    problem3()
    print('='*30)
    problem4()
    print('='*30)
    problem5()
    print('='*30)
    problem6()