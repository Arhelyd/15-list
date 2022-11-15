class Fibo:

    @staticmethod
    def oblicz(n):
        if n in {0, 1}:  
            return n
        return oblicz(n - 1) + oblicz(n - 2)
