class Solution:from typing import List

def maxSum(nums: List[int]) -> int:
    biggest_single_digit = 0
    largest_number = 0
    second_largest_number = 0
    #Runs through array of numbers to find the biggest single digit
    for number in nums:
        for digit in str(number):
            if int(digit)> biggest_single_digit:
                biggest_single_digit = int(digit)
    #Finds the largest and second largest number in the array based on the biggest single digit
    for number in nums:
        for digit in str(number):
            if int(digit) == biggest_single_digit:
                if number > largest_number:
                    second_largest_number = largest_number
                    largest_number = number
                elif number > second_largest_number and number != largest_number:
                    second_largest_number = number
    #Condition to ensure there is no pair in array                
    if 0 == second_largest_number:
        return -1
    return largest_number + second_largest_number
#Print the sum of the two largest numbers in the array
nums = [2536,1613,3366,162]
print(maxSum(nums))
              