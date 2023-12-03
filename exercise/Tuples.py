# https://www.hackerrank.com/challenges/python-tuples/problem

# input
# 2
# 1 2
# output
# -3550055125485641917
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuple = tuple(list(integer_list))
    print(tuple)
    print(hash(tuple))
