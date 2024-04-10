# You are given two Cuboid objects. You need to deep copy the values of object1 into object 2

class Cuboid:
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h

    def getArea(self):
        return self.l * self.h * self.b

    def increaseDimensions(self):
        self.l = self.l + 1
        self.b = self.b + 1
        self.h = self.h + 1

    def deepCopy(self, obj):
        # Your code here
        obj.l = self.l
        obj.b = self.b
        obj.h = self.h

# You are given two objects. Each object has data members X, Y and Z.
# You need to find the nth Fibonacci object. The nth Fibonacci object is given by F(n) = F(n - 1) + F(n - 2); n > 2
# You need to sum the corresponding values of obj1 and obj2 to get obj3.


class FibO:
    def __init__(self, X, Y, Z):
        self.x = X
        self.y = Y
        self.z = Z

    def fiboSum(self, obj):
        self.x += obj.x
        self.y += obj.y
        self.z += obj.z

    def getCoord(self):
        print(self.x, self.y, self.z)

    def deepCopy(self, obj):
        self.x, self.y, self.z = obj.x, obj.y, obj.z


def nthFibO(n, obj1, obj2):
    # Your code here
    if n == 1:
        return obj1
    if n == 2:
        return obj2
    i = 3
    while i <= n:
        temp = obj2
        obj2 = FibO(obj1.x+obj2.x, obj1.y+obj2.y, obj1.z + obj2.z)
        obj1 = temp
        i += 1
    return obj2


# You are given two numbers X and Y. print the sum of X and Y

def sum(X, Y): return X+Y
