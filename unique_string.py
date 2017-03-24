
'''
 author: ylavinia
 
 find if all characters in a string are unique
 create an array with boolean values where the flag at index i
 indicates whether the character at index i is contained in the string
 this method is using bit
 first step is to ask what kind of string it is: ASCII or Unicode
'''


def is_unique_chars(astring):
    checker = 0
    for c in astring:
        #print("c: ", c)
        #print("ord(c) = ", ord(c))
        #print("ord ('a') = ", ord('a'))
        val = ord(c) - ord('a') # so the value is not that big
        #print("val = ", val)
        #print("1 << val: ", bin(1 << val))
        #print("checker & (1 << val) = ", bin(checker & (1 << val)))
        # 1 << val is used to go clear other bits except the bit at index val
        # test bit as A & (1 << bit) is used to test bit
        if (checker & (1 << val) > 0):
            #print("checker & (1 << val) = ", bin(checker & (1 << val)))
            return False
        else:
            checker |= (1 << val) # set bit as A |= (1 << bit) is used to set bit
    return True


# another implementation is using set as set contains only unique elements.
# def is_unique_chars(astring):
#     return len(astring) == len(set(astring))



def main():
    print("This programs determines if all the characters in a string are unique.")
    str = "supermen"
    print("Example: ", str)
    print("Is each character in the string unique? ", is_unique_chars(str))
    str_input = input("Enter a string: ")
    print("Your string: ", str_input)
    print("Is each character in the string unique? ", is_unique_chars(str_input))

if __name__ == "__main__":
    main()


