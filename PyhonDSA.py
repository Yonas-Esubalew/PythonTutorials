# A2SV Class one

import math

class Solution:
    def check_even_odd(self, n): return "Even" if n % 2 == 0 else "Odd"
    def largest_of_three(self, a, b, c): return max(a, b, c)
    def reverse_string(self, s): return s[::-1]
    def is_prime(self, n): return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
    def fibonacci(self, n): a, b = 0, 1; return [a := b, b := a + b][0] for _ in range(n)]
    def factorial(self, n): return 1 if n == 0 else n * self.factorial(n - 1)
    def sum_of_digits(self, n): return sum(int(d) for d in str(n))
    def is_palindrome(self, s): return s == s[::-1]
    def is_number_palindrome(self, n): return str(n) == str(n)[::-1]
    def count_vowels(self, s): return sum(1 for c in s.lower() if c in "aeiou")
    def second_largest(self, lst): return sorted(set(lst), reverse=True)[1] if len(set(lst)) > 1 else None
    def remove_duplicates(self, lst): return list(set(lst))
    def find_gcd(self, a, b): return math.gcd(a, b)
    def decimal_to_binary(self, n): return bin(n)[2:]
    def merge_sorted_lists(self, lst1, lst2): return sorted(lst1 + lst2)
    def sum_of_list(self, lst): return sum(lst)
    def common_elements(self, lst1, lst2): return list(set(lst1) & set(lst2))
    def is_anagram(self, s1, s2): return sorted(s1) == sorted(s2)
    def is_leap_year(self, year): return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    def find_missing_number(self, lst): return (len(lst) + 1) * (len(lst) + 2) // 2 - sum(lst)
    def count_words(self, s): return len(s.split())
    def is_armstrong(self, n): return sum(int(d) ** len(str(n)) for d in str(n)) == n
    def swap_variables(self, a, b): return b, a
    def to_uppercase(self, lst): return [word.upper() for word in lst]
    def fibonacci_recursive(self, n): return n if n <= 1 else self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)

# Example Usage
sol = Solution()
print(sol.check_even_odd(5))  # "Odd"
print(sol.largest_of_three(3, 7, 5))  # 7
print(sol.reverse_string("hello"))  # "olleh"
print(sol.is_prime(7))  # True
print(sol.fibonacci(7))  # [0, 1, 1, 2, 3, 5, 8]
print(sol.factorial(5))  # 120
print(sol.sum_of_digits(123))  # 6
print(sol.is_palindrome("racecar"))  # True
print(sol.is_number_palindrome(121))  # True
print(sol.count_vowels("Hello World"))  # 3
print(sol.second_largest([10, 20, 4, 45, 99]))  # 45
print(sol.remove_duplicates([1, 2, 3, 1, 2, 4]))  # [1, 2, 3, 4]
print(sol.find_gcd(12, 15))  # 3
print(sol.decimal_to_binary(10))  # "1010"
print(sol.merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
print(sol.sum_of_list([1, 2, 3, 4]))  # 10
print(sol.common_elements([1, 2, 3], [2, 3, 4]))  # [2, 3]
print(sol.is_anagram("listen", "silent"))  # True
print(sol.is_leap_year(2024))  # True
print(sol.find_missing_number([1, 2, 4, 5, 6]))  # 3
print(sol.count_words("Hello world! This is Python."))  # 5
print(sol.is_armstrong(153))  # True
print(sol.swap_variables(5, 10))  # (10, 5)
print(sol.to_uppercase(["hello", "world"]))  # ["HELLO", "WORLD"]
print([sol.fibonacci_recursive(i) for i in range(7)])  # [0, 1, 1, 2, 3, 5, 8]

# x =4
# x = "A2SV"
# print(x)

# a = int(input())
# b = int(input())

# print(a+b)
# print(a-b)
# print(a*b)

# a = 12
# b = 23.09
# print(a+b)

b = "hello world"

print(b[2])
print(b[3])
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[5:2:-1])
print(b[::2])
