#Property Tax Function
#Determines the property tax of real estate based on its actual market value.
def property_tax():
    #Get inputs and calculate/format values for actual, assessed, and property tax value.
    act_val = float(input("Enter the actual value: "))
    ase_val = act_val * 0.60
    p_tax = (ase_val / 100) * 0.72
    ase_val = "{:,.2f}".format(ase_val)
    p_tax = "%3.2f" % p_tax
    #Print the output with input and calcualtions conducted in the previous section.
    print("Assessed value: $" + ase_val)
    print("Property tax: $" + p_tax)

def future_value():
    #Gather inputs from user and conduct calculations.
    pres_val = float(input("Enter the present value of the account in dollars: "))
    mo_int_rate = float(input("Enter the monthly interest rate as a percentage: ")) / 100
    months = int(input("Enter the number of months: "))
    fut_val = pres_val * (1 + mo_int_rate) ** months
    #Format and print output based on user inputs.
    print("The information for your account is:")
    pres_val = "%3.2f" % pres_val
    print("Present value: $" + pres_val)
    mo_int_rate = mo_int_rate * 100
    mo_int_rate = "%3.2f" % mo_int_rate
    print("Interest Rate: %" + mo_int_rate)
    fut_val = "%3.2f" % fut_val
    print("After " + str(months) + " months, the value of your account will be $" + fut_val)

def genz_search():
    boy_input = open('BoyNames.txt', 'r')
    popular_boys = boy_input.readlines()
    for i in range(len(popular_boys)):
        popular_boys[i] = popular_boys[i].rstrip('\n')
    girl_input = open('GirlNames.txt', 'r')
    popular_girls = girl_input.readlines()
    boy_input.close()
    girl_input.close()
    for i in range(len(popular_girls)):
        popular_girls[i] = popular_girls[i].rstrip('\n')
    boy_name = input("Enter a boy's name, or N if you do not wish to enter a boy's name: ")
    girl_name = input("Enter a girl's name, or N if you do not wish to enter a girl's name: ")
    if boy_name == "N":
        print ("You chose not to enter a boy's name.")
    elif boy_name in popular_boys:
        print(boy_name + " is one of the most popular boy's names.")
    elif boy_name not in popular_boys:
        print(boy_name + " is not one of the most popular boy's names.")
    if girl_name == "N":
        print("You chose not to enter a girl's name.")
    elif girl_name in popular_girls:
        print(girl_name + " is one of the most popular girl's names.")
    elif girl_name not in popular_girls:
        print(girl_name + " is not one of the most popular girl's names.")

def prime_det(j, dictin):
    dictin[j] = True
    k = 2
    while dictin[j] == True and j > k:
        if j % k == 0:
            dictin[j] = False
        k += 1
def prime_gen():
    num = int(input("Enter an integer greater than 1: "))
    num_list = []
    prime_dict = {}
    for i in range(2, num + 1):
        num_list.append(i)
    for i in range (2, len(num_list) + 2):
        prime_det(i, prime_dict)
        if prime_dict[i] == True:
            print(str(i) + " is a prime.")
        elif prime_dict[i] == False:
            print(str(i) + " is composite.")

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

def recursive_exe(num, exp):
    if exp == 1:
        return (num)
    else:
        return num * recursive_exe(num, exp - 1)

def pow_recursive():
    numb = float(input("Enter a number: "))
    expo = int(input("Enter a positive whole number between 1 and 100: "))
    if expo >= 1 and expo <= 100:
        result = recursive_exe(numb, expo)
    else:
        print("Sorry, that input is not valid. Please try again.")
        pow_recursive()
    result = "{:,.2f}".format(result)
    print(str(numb) + " raised to the power of " + str(expo) + " is " + result)
    

