
# Testar denna function
def func1(x):
    return x + 1

# 3 tester
def test_1():
    assert func1(4) == 5
    
    
def test_2():
    assert func1(10) == 11
    
    
def test_3():
    assert func1(15) == 14                  # Denna ska bli fail
##########################################

# Testar denna function
def func2(x):
    return x + 10
    
# 2 tester
def test_4():
    assert func2(10) == 20
    

def test_5():               # Denna ska bli fail!
    assert func2(15) == 0
    

def test_6():
    assert func2(10) == 20
    

    

    
    

    

    


    
    

