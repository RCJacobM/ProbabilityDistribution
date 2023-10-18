class ProbabilityDistribution:
    """
    Create a Probability Distribution table:
    table = ProbabilityDistribution({1: 1/7, 6: 1/7, 11: 1/7, 16: 1/7, 21: 1/7})

    where:
    x: keys
    P(x): values (decimals or fractions)
    In P(x) fractions can be defined by dividing the numerator to the denominator

    Calculations
    table = ProbabilityDistribution({1: 1/7, 6: 1/7, 11: 1/7, 16: 1/7, 21: 1/7})

    Mean:
    table.mean() | Expected output: 7.86

    Variance:
    table.variance() | Expected output: 42.76

    Standard Deviation:
    table.standardDeviation() | Expected output: 6.54
    
    """
    def __init__(self, data):
        self.x = list(data.keys())
        self.Pofx = list(data.values())

    def mean(self):
        return round(sum([i * j for i, j in zip(self.x, self.Pofx)]), 2) # μ
    
    def variance(self):
        mean = round(sum([i * j for i, j in zip(self.x, self.Pofx)]), 2)
        xMinusMean = [i - mean for i in self.x] # x - μ
        xMinusMeanSquared = [i * i for i in xMinusMean] # (x - μ)^2
        xMinusMeanSquaredTimesPofx = [i * j for i,j in zip(xMinusMeanSquared, self.Pofx)] # (x - μ)^2 ⋅ P(x)
        return round(sum(xMinusMeanSquaredTimesPofx), 2) # σ^2
    
    def standardDeviation(self):
        mean = round(sum([i * j for i, j in zip(self.x, self.Pofx)]), 2)
        xMinusMean = [i - mean for i in self.x] # x - μ
        xMinusMeanSquared = [i * i for i in xMinusMean] # (x - μ)^2
        xMinusMeanSquaredTimesPofx = [i * j for i,j in zip(xMinusMeanSquared, self.Pofx)] # (x - μ)^2 ⋅ P(x)
        variance = round(sum(xMinusMeanSquaredTimesPofx), 2) # σ^2
        return round(variance ** .5, 2) # σ
