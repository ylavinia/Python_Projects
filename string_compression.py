'''
author: ylavinia

String compression
Implement a method to perform basic string compression using the counts of
repeated characters.
Example:
Input: aabcccccaa
Output: a2b1c5a2
Assume the string has only uppercase and lowercase letters.
'''

def compress_string(astring):
    char_and_freq = create_freq_list(astring)
    return ''.join(char_and_freq)

def create_freq_list(astring):
    freq_list = []
    count = 0
    for i in range(len(astring)):
        # increment count until either the next index is greater than
        # the string length or the nex letter is not the same as the current
        count += 1
        if ((i + 1) >= len(astring) or (astring[i + 1] != astring[i])):
            # append the character
            freq_list.append(astring[i])
            # append the current count
            freq_list.append(str(count))
            # count rolls back to zero since we're' moving to the next letter
            count = 0

    return freq_list



def main():
    print("This program compresses the patterns in a string by replacing the pattern with the count of the repeated characters.")
    print("Example:")
    astring = "aaaaaaaaabbbbbbcccccaaaa"
    print("The string: ", astring)
    print("Compressed: ", compress_string(astring))
    str_input = input("Enter a string with duplicate letters, ex. aboegggguuurryy@@@: ")
    print("Your string: ", str_input)
    print("Compressed: ", compress_string(str_input))


if __name__ == "__main__":
    main()

