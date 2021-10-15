def encode(message):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        '''first while loop is for going through each letter'''
        count = 1
        ch = message[i]
        j = i #assign current letter index to j in order to count the occurrence of letters
        print(ch)
        print('this is j', j)
        print('this is i ', i)

        while (j < len(message)-1): # to loop from particular letter till the end

            '''if the character at the current index is 
            the same as the character at the next index. 
            If the characters are the same, the count is incremented to 1'''
            if (message[j] == message[j + 1]): #if the letters are equal to each other, e.g. A == A, keep looping, else break
                count = count + 1
                j = j + 1
            else:
                break
        '''the count and the character is concatenated to the encoded string'''
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string

encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)
