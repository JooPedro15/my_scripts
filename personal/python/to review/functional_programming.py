# Functional programming
"""
map
iterate through an iterable and apply a function
the result will be stored in a new object
"""


def multiply_by2(item):
    return item * 2


a = list(map(multiply_by2, [1, 2, 3]))

print(a)

"""
filter
iterate through the items and filter the results (True)
"""


def check_odd(item):
    return item % 2 != 0


print(list(filter(check_odd, [1, 2, 3])))

"""
zip
zip multiple iterables together
"""

my_list = [1, 2, 3]
your_list = [10, 20, 300]
their_list = [100, 200, 300]
print(list(zip(my_list, your_list, their_list)))

"""
reduce
apply and expression and accumulate the result to the next iteration
"""

from functools import reduce


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 0))


def highest_num(acc, item):
    return acc if item < acc else item


print(reduce(highest_num, my_list, 0))

"""
lambda expressions
when we only want to use the expression once
anonymous function
lambda parameter: action(parameter)
"""

print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda item, acc: item + acc, my_list, 0))

"""
List comprehensions

my_list = [param for param in iterable]
"""

my_list = [char for char in 'hello']

print(my_list)

num_list = [i * 2 for i in range(0, 100)]

print(num_list)

num_list2 = [i * 2 for i in range(0, 100) if i % 2 == 0]

print(num_list2)


"""
Dictionary comprehensions
"""

simple_dic = {
    'a': 1,
    'b': 2
}

my_dict = {(key + 'final'): value ** 2 for key, value in simple_dic.items() if value % 2 == 0}

print(my_dict)

my_dict2 = {num: num * 2 for num in [1, 2, 3] if num % 2 != 0}

print(my_dict2)