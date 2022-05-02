from craps import Checker


def test_empty_history():
    checker = Checker()
    result = checker.check([])
    assert result == 0


def test_7_on_first_row():
    checker = Checker()
    result = checker.check([7])
    assert result == 1

def test_11_on_first_row():
    checker = Checker()
    result = checker.check([11])
    assert result == 1

def test_2_on_first_row():
    checker = Checker()
    result = checker.check([2])
    assert result == -1

def test_3_on_first_row():
    checker = Checker()
    result = checker.check([3])
    assert result == -1

def test_12_on_first_row():
    checker = Checker()
    result = checker.check([12])
    assert result == -1

def test_6_return_0():
    checker = Checker()
    result = checker.check([6])
    assert result == 0 

def test_6_6_return_1():
    checker = Checker()
    result = checker.check([6,6])
    assert result == 1 

def test_6_7_return_neg1():
    checker = Checker()
    result = checker.check([6,7])
    assert result == -1 

def test_6_x_6_return_1():
    checker = Checker()
    result = checker.check([6,2,3,4,5,8,9,10,11,12,6])
    assert result == 1 

def test_6_xreturn_0():
    checker = Checker()
    result = checker.check([6,2,3,4,5,8,9,10,11,12])
    assert result == 0 

def test_6_x_7_return_neg1():
    checker = Checker()
    result = checker.check([6,2,3,4,5,8,9,10,11,12,7])
    assert result == -1 
