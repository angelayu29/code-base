import sys
import math

EPSILON = 1e-7


def sqrt(num, epsilon):
    if num < 0:
        return math.nan
    if num == 0 or num == math.inf or math.isnan(num):
        return num
    currentGuess = num
    while True:
        previousGuess = currentGuess
        currentGuess = 0.5 * (previousGuess + num / previousGuess)
        if abs(currentGuess - num) < epsilon:
            break
    return currentGuess

def main():
    if len(sys.argv) <= 1 or len(sys.argv) > 3:
        sys.stderr.write("Usage: python sqrt.py <value> [epsilon]\n" % sys.argv[0])
        sys.exit(1)
    try:
        num = float(sys.argv[1])
    except ValueError:
        sys.stderr.write("Error: Value argument must be a double.\n")
        sys.exit(1)
    epsilon = EPSILON
    if len(sys.argv) == 3:
        try:
            epsilon = float(sys.argv[2])
            if epsilon <= 0:
               raise ValueError
        except ValueError:
            sys.stderr.write("Error: Epsilon argument must be a positive double.\n")
            sys.exit(1)


    print(f"{sqrt(num, epsilon):.8f}")
    sys.exit(0)



if __name__ == "__main__":
    main()