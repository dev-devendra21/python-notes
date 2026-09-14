class A:
    label = "A: blend"

class B(A):
    label = "B: blend"

class C(A):
    label = "C: blend"


class D(B, C):
    pass 


d = D 

print(d.label)
print(D.__mro__)