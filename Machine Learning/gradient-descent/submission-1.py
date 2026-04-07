class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float: 
        def f(x):
            return 2*x

        for i in range(iterations):
            init -= learning_rate*f(init) 
        return round(init,5)

    