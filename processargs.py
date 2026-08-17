import sys


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python %s <num 1> <num 2>" % sys.argv[0])
        sys.exit(1)

    nums = [0] * 2
    for i in range(1,3):
        try:
            nums[i-1] = int(sys.argv[i])
        except ValueError:
            sys.stderr.write("Error: Argument '%s' is not an integer." % sys.argv[i])
            sys.exit(1)
    print("max(%d, %d, %d)" % (nums[0], nums[1], max(nums[0], nums[1])))



if __name__ == "__main__":
    main()