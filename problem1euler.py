
"""

import math
import pandas as pd

def main():
   n = 1000
   multi = []
   for i in range(1, n):
       if (i % 3 == 0) or (i % 5 == 0):
        multi.append(i)

   df = pd.DataFrame({'multis': multi})
   print(df['multis'].sum())


if __name__ == '__main__':
    main()

"""


total = 0
for i in range(3,1000):
    if (i % 3 == 0) or (i % 5 == 0):
        total += i
print(total)