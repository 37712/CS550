def polyval(fpoly, x):
    """polyval(fpoly, x)
    Given a set of polynomial coefficients from highest order to x^0, compute the value of the polynomial at x. We assume zero coefficients are present in the coefficient list/tuple.
    Example: f(x) = 4x^3 + 0x^2 + 9x^1 + 3 evaluated at x=5 polyval([4, 0, 9, 3], 5))
    returns 548
    """
    fpoly_size = len(fpoly)
    y_value=0
    for i in range(len(fpoly)):
        y_value += fpoly[i]*(x**(fpoly_size-(i+1)))
    return y_value

test_poly = [4,0,9,3]
test_derivative = polyval(test_poly,5)


def derivative(fpoly):
    """derivative(fpoly)
    Given a set of polynomial coefficients from highest order to x^0, compute the derivative polynomial. We assume zero coefficients are present in the coefficient list/tuple.
    Returns polynomial coefficients for the derivative polynomial. Example:
    derivative((3,4,5)) # 3 * x**2 + 4 * x**1 + 5 * x**0 returns: [6,4] #6*x**1+4*x**0
    """
    fpoly_size = len(fpoly)
    fpoly_derivative = []
    for i in range(len(fpoly)-1):
        derivative_coefficient = (fpoly_size - (i+1)) * fpoly[i]
        fpoly_derivative.append(derivative_coefficient)
    return fpoly_derivative

def NewtonRaphson(fpoly, a, tolerance = .00001):
    """Given a set of polynomial coefficients fpoly for a univariate polynomial function,
    e.g. (3, 6, 0, -24) for 3x^3 + 6x^2 +0x^1 -24x^0, find the real roots of the polynomial (if any) using the Newton-Raphson method.
    """

    """a is the initial estimate of the root and
    starting state of the search
    This is an iterative method that stops when the change in estimators is less than tolerance."""
    poly_a = polyval(fpoly,a)
    gradient = polyval(derivative(fpoly),a)
    print("poly_a = ",poly_a," gradient = ",gradient)
    x_cur = a - poly_a/gradient
    x_prev = a
    print("x_prev = ",x_prev," x_cur = ",x_cur)
    # linear approximation until difference is <= tolerance
    print(abs(x_cur-x_prev))
    print(tolerance)
    while(abs(x_cur-x_prev)>tolerance):
        poly_x = polyval(fpoly,x_prev)
        gradient = polyval(derivative(fpoly),x_prev)
        print("poly_a = ",poly_a," gradient = ",gradient)
        x_prev =x_cur
        x_cur = x_prev - poly_x/gradient
        print("x_prev = ",x_prev," x_cur = ",x_cur)
    return x_cur

root = NewtonRaphson( [7, 3, -5, 32, -7], 5)
print("root = ", root)
