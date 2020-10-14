import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return (self.real == other.real and self.imaginary == other.imaginary)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    # a + i * b by another c + i * d gives: 
    # (a + i * b) / (c + i * d) = 
    # (a * c + b * d)/(c^2 + d^2) + (b * c - a * d)/(c^2 + d^2) * i.
    # which is not exactly what I understood from khan academy...

    def __truediv__(self, other):
        realPart = (self.real * other.real + self.imaginary * other.imaginary)
        imaginaryPart = (self.imaginary * other.real - self.real * other.imaginary)
        scale = (other.real ** 2 + other.imaginary ** 2)
        return ComplexNumber(realPart / scale, imaginaryPart / scale)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)


    def exp(self):
        return ComplexNumber(math.exp(self.real), )
