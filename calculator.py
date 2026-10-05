# Basic Calculator
# Doc lines and Hints perposefully omitted
def add (a, b):
    return (a + b)

def sub (a, b):
    return ( a - b)

def mult (a , b):
    return (a* b)

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Error")
    return a / b

# Financial Calculator (Extra Credit? :p)

def pv(rate, nper, pmt, fv=0):
    return fv / (1 + rate)**nper

def npv(rate, cashflows):
    total = 0
    for i, cf in enumerate(cashflows, start=1):
        total += cf / (1 + rate)**i
    return total

def simple_interest(p, r, t):
    return p * r * t

# Testing

def run_tests():
    # add
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(0, 0) == 0  

    # sub
    assert sub(10, 4) == 6
    assert sub(4, 10) == -6
    assert sub(5, 5) == 0

    # mult
    assert mult(3, 4) == 12
    assert mult(-2, 3) == -6
    assert mult(5, 0) == 0

    # div
    assert div(9, 3) == 3
    assert div(1, 4) == 0.25
    assert div(-8, 2) == -4

    try:
        div(5, 0)
        assert False, "div(5, 0) should raise ZeroDivisionError"
    except ZeroDivisionError:
        pass

    print("All tests passed!")

def main():
    run_tests()
    print("PV:", pv(0.05, 10, 0, fv=10000))
    print("NPV:", npv(0.10, [-1000, 300, 400, 500]))
    print("Simple Interest:", simple_interest(1000, 0.05, 3))

if __name__ == "__main__":
    main()
