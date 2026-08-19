
def main():
    values = [0] * 10
    print(values)
    values.append(1)
    print(values)

    values = [2 * num for num in range(11)]
    print(values)
    '''
    print(values[3])
    print(values[1:5])
    print(values[:])
    print(values[::-1])
    print(values[-1])
    '''

    zeros = [0] * 5
    ones = [1] * 5
    zeros.extend(ones)
    print(zeros)
    zeros.insert(5, 2)
    print(zeros)
    zeros.remove(2)
    print(zeros)
    zeros.pop()
    print(zeros)
    print(zeros.index(1))
    zeros.insert(0,2)
    print(zeros)
    print(sorted(zeros))
    zeros.sort()
    print(zeros)

    copy = zeros.copy()
    copy[0] = 10
    print(zeros)
    print(copy)

if __name__=="__main__":
    main()