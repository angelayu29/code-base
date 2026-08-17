import math
import pandas as pd

def main():
   n = 20
   multi = 0

   def fibonacci_generator():
       term1, term2 = 1, 2
       while True:
           yield term1
           term1, term2 = term2, term1 + term2

   # Example usage:
   gen = fibonacci_generator()
   for _ in range(n):
       print(next(gen), end=" ")

   for _ in range(1, n):
       if _ % 2 == 0:
        multi = multi + _



if __name__ == '__main__':
    main()