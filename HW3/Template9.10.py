# The get_word_dict function returns a dictionary containing
# the words from line_list as keys, and their line numbers
# as values.
def get_word_dict(line_list):
    
    # Create a dictionary to hold the words.
    word_dict = {}
    # Step through the list of lines.
    for e in line_list:
        # Split the line into words.
        words = e.split(' ')

        # Step through the list of words.
        for w in words:
            # If the word is in the dictionary...
            if w in word_dict:
                # Update the existing value.
                #YOUR CODE HERE
                word_dict[w] += 1
            else:
                # Otherwise, store the word in the dictionary. set the count to 1. 
                #YOUR CODE HERE
                word_dict[w] = 1
    # Return the dictionary.
    return(word_dict)

# The write_index_file function writes an index file containing the
# elements of the word_dict dictionary.
def write_index_file(word_dict):
    # Open the file.
    outputfile = open('index_j.txt', 'w')
    key_dict = sorted(word_dict)
    # Write the entries from the dictionary.
    for key in key_dict:
        # Write the word to the dictionary
        outputfile.write(str(key) + ' ' + str(word_dict[key]))
        outputfile.write('\n') #this writes a space to the line

    # Close the file.
    outputfile.close()
    
def main():
    # Open the file.
    inputfile = open('tirole_nobel.txt', 'r')

    # Read the file's contents into a list.
    line_list = inputfile.readlines()
    #sorted(line_list)
    # Close the file.
    inputfile.close()
    # Strip the newline from each list element.
    for i in range(len(line_list)):
        line_list[i] = line_list[i].rstrip('\n')
    # Get a dictionary holding the words and their line numbers.
    word_dict = get_word_dict(line_list)
    # Write the index file.
    write_index_file(word_dict)
    
main()
