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
