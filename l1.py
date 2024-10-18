from typing import List

def maxSum(nums: List[int]) -> int:
    biggest_single_digit = 0
    largest_number = 0
    second_largest_number = 0
    for number in nums:
        for digit in str(number):
            if int(digit)> biggest_single_digit:
                biggest_single_digit = int(digit)
    for number in nums:
        for digit in str(number):
            if int(digit) == biggest_single_digit:
                if number > largest_number:
                    second_largest_number = largest_number
                    largest_number = number
                elif number > second_largest_number:
                    second_largest_number = number
    if 0 == second_largest_number:
        return -1
    return largest_number + second_largest_number
nums = [2536,1613,3366,162]
print(maxSum(nums))
    