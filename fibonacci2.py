# class Fib:
#     def __init__(self, max):
#         self.max = max       
# #	What is self.max? It’s an instance variable. It is completely separate from max, which was passed into the __init__() method as an argument. self.max is “global” to the instance. That means that you can access it from other methods.

class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        # this works because it sets the next value to sum of the previous two values
        self.a, self.b,  = self.b, self.a + self.b
        return fib