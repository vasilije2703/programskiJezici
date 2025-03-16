
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
        
    def __add__(self, z):
        return Complex(self.r + z.r, self.i + z.i)
    
    def __sub__(self, z):
        return Complex(self.r - z.r, self.i - z.i)
    
    def __mul__(self, z):
        return Complex(self.r * z.r - self.i * z.i, self.r * z.i + self.i * z.r)
    
    def __str__(self):
        return f'{self.r} + {self.i}i ' if self.i > 0 else f'{self.r} - {self.i}i'
        
    def __eq__(self,z):
        return self.r == z.r and self.i == z.i
    
    def __abs__(self):
          if self.r < 0:
              self.r *= (-1)

          if self.i < 0:
              self.i *= -1   

          return self    
    

z1 = Complex(-2, 5)
z2 = Complex(1, 3)

print(z1 + z2)
print(z1 - z2)
print(z1*z2)
print(z1 == z2)
print(abs(z1))