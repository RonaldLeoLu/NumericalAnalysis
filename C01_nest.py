# 0.1 exercise 1
# use function 'nest' to estimate the value of
# P(x) = 1+x+x^2+...+x^50 where x=1.00001

def nest(d,c,x,b=None):
    '''
    calculate the value of polynomial with Horner'rule

    Input:
    - d : degree of polynomial
    - c : d+1-D array, the coefficients
    - x : the variable
    - b : optional

    Output:
    - y : the value of P(x)
    '''
    if b is None:
        b = [0] * (d+1)

    y = c[-1]
    for i in range(d-1, -1, -1):
        y = y * (x - b[i]) + c[i]

    return y

if __name__ == '__main__':
    # Problem1
    d, c, x = 50, [1] * 51, 1.00001
    print(nest(d, c, x))
    print((x**51 - 1)/(x - 1))
    # Problem2
    d, c, x = 99, [1, -1] * 50, 1.00001
    print(nest(d, c, x))
    print(-(x**100 - 1) / (x + 1))