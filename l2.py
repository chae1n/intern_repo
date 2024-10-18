from typing import List

#Function to find two numbers in a list that add up to a given target
def twoSum(nums: List[int], target: int) -> List[int]:
    #Using for loop to look through the list of integers 
    for number in nums:
        #Find the two integers to total the target sum
        print(number)
        number1 = number
        print("Number 1: {number1}")


        #Return the two integers

nums = [2, 7, 11, 15]
target = 9
#Expected output: [0, 1]
print(twoSum(nums, target))