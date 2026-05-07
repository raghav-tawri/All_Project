# 1. Count Character Frequency: Write a function that takes a string and returns a dictionary
# where the key is the character and the value is the number of times that character appears.
# Example: Input 'banana' → Output {'b':1, 'a':3, 'n':2}.
def count_char(s):
    frq = {}
    for char in s:
        if char in frq:
            frq[char] += 1
        else:
            frq[char] = 1
    return frq

# 2 Merge Two Dictionaries with Sum: Given two dictionaries containing integer values, merge
# them. If a key appears in both dictionaries, add their values. Example: d1={'a':10,'b':20},
# d2={'b':5,'c':15} → Output {'a':10,'b':25,'c':15}.
def merge_dict(d1, d2):
    merged = d1.copy()
    for k, v in d2.items():
        if k in merged:
            merged[k] += v
        else:
            merged[k] = v
    return merged

# 3 Group Words by First Letter: Given a list of words, create a dictionary where the key is the
# first letter and the value is the list of words starting with that letter. Example:
# ['apple','ant','banana','ball'] → {'a':['apple','ant'], 'b':['banana','ball']}.
def group_words(ws):
    grouped = {}
    for w in ws:
        f_let = w[0]
        if f_let in grouped:
            grouped[f_let].append(w)
        else:
            grouped[f_let] = [w]
    return grouped

# 4  Group Numbers by Even and Odd: Given a list of numbers, create a dictionary with keys
# 'even' and 'odd' and store numbers accordingly. Example: [1,2,3,4,5] →
# {'odd':[1,3,5],'even':[2,4]}.
def group_numbers_by_even_odd(numbers):
    grouped = {'even': [], 'odd': []}
    for n in ns:
        if n % 2 == 0:
            grouped['even'].append(n)
        else:
            grouped['odd'].append(n)
    return grouped

# 5 Check if All Values are Unique: Write a function that checks if all values in a dictionary are
# unique. Example: {'a':1,'b':2,'c':3} → True, {'a':1,'b':2,'c':1} → False.
def value_unique(d):
    values = set()
    for v in d.values():
        if v in values:
            return False
        values.add(v)
    return True

# 6 Valid Parenthesis: Given a string containing brackets (), {}, [], determine if the string is valid.
# A string is valid if every opening bracket has a corresponding closing bracket of the same type
# and in the correct order.
def is_valid_parenthesis(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    return len(stack) == 0
