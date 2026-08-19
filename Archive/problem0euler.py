import math
import pandas as pd
import time

def main () :
    n = 1
    squares = []
    nmax = 655000
    while n <= nmax :
        square = n * n
        print(square)
        squares.append(square)
        n += 2

    df = pd.DataFrame({'square': squares})
    print(df)
    print(df['square'].sum())


if __name__=='__main__' :
    start_time_ = time.perf_counter()

    main()

    end_time_ = time.perf_counter()

    execution_time = end_time_ - start_time_
    print(f"Execution time: {execution_time:.6f} seconds")
