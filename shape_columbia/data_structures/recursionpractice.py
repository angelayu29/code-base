import string

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def length(s):
    if s == "":
        return 0
    return 1 + length(s[1:])

def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y - 1)

def power_tail(x, y):
    def power_tail_helper(x, y, result):
        if y == 0:
            return result
        return power_tail_helper(x, y - 1, x * result)
    return power_tail_helper(x, y, 1)

def factorial_tail(n):
    def factorial_tail_helper(n, result):
         if n == 0:
            return result
         return factorial_tail_helper(n - 1, n * result)
    return factorial_tail_helper(n, 1)


def remove_vowels(s):
    if len(s) == 0:
        return ""
    c = s[0]
    if c in ('a', 'e', 'i', 'o', 'u'):
        return remove_vowels(s[1:])
    return c + remove_vowels(s[1:])

def remove_vowels_tail(s):
    def remove_helper(s, result):
        if s == "":
            return result
        c = s[0]
        if c in ('a', 'e', 'i', 'o', 'u'):
            return remove_helper(s[1:], result)
        return remove_helper(s[1:], result + s[0])
    return remove_helper(s[1:], "")

if __name__ == "__main__":
    print(remove_vowels_tail('elephant'))
