# task 1: Напишіть функцію, яка обчислює добуток елементів списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

# import random
#
# def create_random_list(length, min_num, max_num):
#     return [random.randint(min_num, max_num) for _ in range(length)]
#
# def multiply_list_nums(input_list):
#     result = 1
#     for num in input_list:
#         result *= num
#     return result
#
# random_list = create_random_list(7, 1, 10)
# product = multiply_list_nums(random_list)
#
# print(f"Our list: {random_list}")
# print(f"Product of numbers in the list: {product}")

# task 2 Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
# import random
#
# def create_random_list(length, min_num, max_num):
#     return [random.randint(min_num, max_num) for _ in range(length)]
#
# def find_min_num(input_list):
#     min_num = min(input_list)
#     return(min_num)
#
# random_list = create_random_list(7, 1, 10)
# min_num = find_min_num(random_list)
#
# print(f"Our list: {random_list}")
# print(f"Minimal number: {min_num}")

#task 3: Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
# import random
#
# random_list = [random.randint(-9, 37) for _ in range(10)]
#
# def is_prime(number):
#     if number <= 1:
#         return False
#     for _ in range(2, number):
#         if number % _ == 0:
#             return False
#     return True
#
# def find_primes_in_list(input_list):
#     prime_numbers = []
#     for num in input_list:
#         if is_prime(num):
#             prime_numbers.append(num)
#     return prime_numbers
#
# print(f"Our list: {random_list}")
# prime_numbers = find_primes_in_list(random_list)
# if prime_numbers:
#     print(f"Here are the prime numbers we found in the list: {prime_numbers}")
#     print(f"The number of prime numbers: {len(prime_numbers)}")
# else:
#     print("No prime numbers in the list, sorry.")
