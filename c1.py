# Does a given string have balanced pairs of brackets? 
# Given a string as input, return True or False depending on whether the 
# string contains balanced (), {}, [], and/or <>.

def has_balanced_brackets(phrase):
    bracket_map = {')': '(', '}': '{', ']': '[', '>': '<'}
    stack = []

    for char in phrase:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack.pop() != bracket_map[char]:
                return False
    
    return len(stack) == 0

input_str = input("Enter a phrase: ")
result = has_balanced_brackets(input_str)
print(result)