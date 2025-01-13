import calc


def test_add():
    if calc.add(1,2) == 3:
        print("Test add(a,b) is OK")
    else:
        print("Test add(a,b) is fail")

def test_sub():
    if calc.sub(3, 1) == 2:
        print("Test add(a,b) is OK")
    else:
        print("Test add(a,b) is fail")

def test_mul():
    if calc.mul(2, 2) == 4:
        print("Test add(a,b) is OK")
    else:
        print("Test add(a,b) is fail")

def test_div():
    if calc.div(4, 2) == 2:
        print("Test add(a,b) is OK")
    else:
        print("Test add(a,b) is fail")

test_add()
test_sub()
test_mul()
test_div()