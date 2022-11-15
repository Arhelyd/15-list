class Fibo:

   # @staticmethod
   # def oblicz(n):
   #     if n in {0, 1}:  
   #         return n
   #     return Fibo.oblicz(n - 1) + Fibo.oblicz(n - 2)
   
   #na początku przez pomyłkę zrobiłem rekurencyjnie to teraz dodałem iteracyjnie
    
    @staticmethod
    def oblicz_iter(n):
        a,b = 0,1
        for i in range(n):
            a,b = b,a+b
        return a

    def oblicz(n):
        if n in {0, 1}:  
            return n
        return Fibo.oblicz(n - 1) + Fibo.oblicz(n - 2)
    def isPerfectSquare(x):
        s = int(math.sqrt(x))
        return s*s == x
    @staticmethod
    def checkIsItFiboElement(n):
        return Fibo.isPerfectSquare(5*n*n + 4) or Fibo.isPerfectSquare(5*n*n - 4)
    

