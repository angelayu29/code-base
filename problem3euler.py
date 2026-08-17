import math
import time

def main():
    n=600851475143
    # Factors Repeat after the floor of the sqrt(n), so stop there.
    div = 2
    while n % div == 0:
        print(div)
        n //=div
    div += 1
    max_factor = int(math.sqrt(n))
    while div <= max_factor:
        if n % div == 0:
            # We found a prime factor
            print(div)
            n //= div
            max_factor = int(math.sqrt(n))
        else:
            div += 2
    # This one is the largest prime factor
    if n != 1:
        print(n)


if __name__=='__main__' :
    start_time_ = time.perf_counter()
    
    main()

    end_time_ = time.perf_counter()

    execution_time = end_time_ - start_time_
    print(f"Execution time: {execution_time:.6f} seconds")

