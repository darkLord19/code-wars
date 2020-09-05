# Write a program to reverse digits of a number

# O(Log(n))
def reverse_num_digits(num):
    rev_num = 0
    neg = False
    if num < 0:
        neg = True
        num = -1 * num
    while num != 0:
        t = num % 10
        num = int(num / 10)
        rev_num = rev_num * 10 + t
    if neg:
        return -1 * rev_num
    return rev_num


if __name__ == "__main__":
    n = int(input())
    print(reverse_num_digits(n))
