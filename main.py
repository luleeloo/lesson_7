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

# task 4
# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.

# import random
#
# random_list = [random.randint(1, 20) for _ in range(10)]
#
# def remove_num_from_list(input_list, num_to_remove):
#     count_removed = 0
#     while num_to_remove in input_list:
#         input_list.remove(num_to_remove)
#         count_removed += 1
#     return count_removed
#
# print(f"Our list: {random_list}")
#
# while True:
#     try:
#         num_to_remove = int(input("Enter the number you want to remove from our list: "))
#         if num_to_remove in random_list:
#             count_removed = remove_num_from_list(random_list, num_to_remove)
#             print("\n")
#             print(f"Removed number of elements: {count_removed}; here is/are the element(s): {num_to_remove}.")
#             print(f"Updated list: {random_list}")
#             break
#         else:
#             print("No such a number in the list. Please try again.")
#     except ValueError:
#         print("Wrong format")

# task 5
# Напишіть функцію, яка отримує два списки як параметр і
# повертає список, що містить елементи обох списків.

# import random
#
# def merge_lists(list1, list2):
#     for item in list2:
#         list1.append(item)
#     return list1
#
# # Generating random numbers with a chance of overlap
# list1 = [random.randint(1, 20) for _ in range(5)]
# print(f"List 1: {list1}")
# list2 = [random.randint(15, 27) for i in range(5)]
# print(f"List 2: {list2}")
#
# result = merge_lists(list1, list2)
# print(f"Merged lists: {result}")

