class Fibo:

    @staticmethod
    def oblicz(n):
        if n in {0, 1}:  
            return n
        return Fibo.oblicz(n - 1) + Fibo.oblicz(n - 2)

