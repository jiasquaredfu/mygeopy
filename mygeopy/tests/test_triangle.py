from mygeopy.triangle import hypot
def test_hypot():
    assert hypot(0,0) == 0, "Non-zero inputs"
    assert hypot(-1,1) == None, "NaN output"
    assert hypot(3,4) == 5
    #assert hypot(12,16) == 20
