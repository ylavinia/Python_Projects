'''
author: ylavinia

Given a string, check if it is a permutation of a palindrome.
Example:
Input: Tact Coa
Output: True
        (permutations: "taco cat", "atco cta")

A way to solve is to look into the definition of palindrome.
For a string with even number of characters, all characters must be an even
number count.
For a string with odd number of characters, only one character can have
an odd number count and others must have an even number count.
'''

def is_permutation_of_palindrome(astring):
    print("The string is: ", astring)
    char_count = create_frequency_table(astring)
    return has_max_one_odd(char_count)

def has_max_one_odd(char_count):
    foundOdd = False
    for k, v in char_count.items():
        if v % 2 == 1:
            if foundOdd == True:
                return False # has more than one odd freq
            else:
                foundOdd = True # find the first odd freq
    return True # it has only one odd frequency

def get_numeric_number(c):
    a = ord('a') - ord('a')
    z = ord('z') - ord('a')
    val = ord(c) - ord('a')
    # print(val)
    return val

def create_frequency_table(astring):
    freq_table = dict.fromkeys(astring, 0)
    for c in astring:
        x = get_numeric_number(c)
        if (x >= 0): # we don't consider non-char like whitespace
            freq_table[c] += 1
    return freq_table



def main():
    print("Given a string, check if it is a permutation of a palindrome.")
    print("===== Examples===============================================")
    print("is it a permutation of palindrome? ", is_permutation_of_palindrome("don't nod"))
    print("is it a permutation of palindrome? ", is_permutation_of_palindrome("taco cat"))
    print("is it a permutation of palindrome? ", is_permutation_of_palindrome("hemoglobin"))
    print("=============================================================")
    string_input = input("Enter a string: ")
    print("is it a permutation of a palindrome? ", is_permutation_of_palindrome(string_input))

if __name__ == "__main__":
    main()




