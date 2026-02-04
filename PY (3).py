def test(a,b):
    if a<b:
        return test(a,b-2)+test(a-1,b-3)+6