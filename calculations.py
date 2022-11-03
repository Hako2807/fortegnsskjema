import pylab

class Calculate:
    def __init__(self) -> None:
        pass

    def f(self, x):
        ans = 0
        for i, constant in enumerate(self.constants):
            ans += constant * x ** (self.degree - i)
        return ans
    
    def make_function(self):
        self.degree = 0
        self.degree = int(input("which degree is your polyniomial equation in? "))
        self.constants = [0 for _ in range(self.degree+1)]
        for i in range(self.degree+1):
            self.constants[i] = int(input(f"what is the constant before x^{self.degree-i}? "))

    
    def factorize_second_degree(self):
        if self.degree == 2:
            d = self.constants[1]**2 - 4 * self.constants[0] * self.constants[2]
            if d < 0:
                factors = [0, 0, 0]
                return factors
            
            x1 = (- self.constants[1] + (d)**0.5) / (2 * self.constants[0])
            x2 = (- self.constants[1] - (d)**0.5) / (2 * self.constants[0])

            factors = [self.constants[0], x1, x2]
        
        return factors
    
    def choose_range(self):
        minimum = int(input("Choose a lower bond: "))
        maximum = int(input("Choose a higher bond:"))
        return pylab.linspace(minimum, maximum, (maximum-minimum)*10)
    
    def calculate_fortegn(self, factors: list):
        x_range = self.choose_range(self)
        self.first_factor = [1 if factors[0] > 0 else -1]
        self.second_factor = [1 if x > factors[1] else -1 for x in x_range]
        self.third_factor = [1 if x > factors[0] else -1 for x in x_range]
        print(self.first_factor)
        print(self.second_factor)
        print(self.third_factor)