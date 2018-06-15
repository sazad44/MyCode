# README:
#  * Edit this file where noted to complete exercises.
#  * DO NOT change function names or your code will not pass test cases.
#  * Output must match the reference solution's output EXACTLY, examples of
#    reference solution output will be provided throughout the document.

# Exercise 2-6
# PROMPT(S) (Example user input of '100'):
'''
Enter the amount of the purchase: 100
'''
# OUTPUT:
'''
Purchase Amount: 100.00
State Tax: 5.00
County Tax: 2.50
Total Tax: 7.50
Sale Total: 107.50
'''
def sales_tax():
	# your code here
	st_tax = 5.00
	co_tax = 2.50
	to_tax = (st_tax + co_tax)/100
	print("")
	pur_amount = float(input("Enter the amount of the purchase: "))
	sale_total = pur_amount + (pur_amount*to_tax)
	sale_total = " %3.2f" % sale_total
	st_tax = " %3.2f" % 5.00
	co_tax = " %3.2f" % 2.50
	to_tax = " %3.2f" % (to_tax*100)
	pur_amount = " %3.2f" % pur_amount
	# defined variables either through input or calculation; formatted decimals
	print("")
	print("Purchase Amount:" + str(pur_amount))
	print("State Tax:" + str(st_tax))
	print("County Tax:" + str(co_tax))
	print("Total Tax:" + str(to_tax))
	print("Sale Total:" + str(sale_total))
	print("")
	#printed output of pertinent information

# Exercise 2-14
# PROMPT(S) (Example user input of '100', '5', '12', and '10'):
'''
Enter the starting principal: 100
Enter the annual interest rate: 5
How many times per year is the interest compounded? 12
For how many years will the account earn interest? 10
'''
# OUTPUT:
'''
At the end of 10 years you will have $ 164.70
'''
def compound_interest():
	# your code here
	p = float(input("Enter the starting principal: "))
	r = float(input("Enter the annual interest rate: "))
	r /= 100
	n = float(input("How many times per year is the interest compounded? "))
	t = int(input("For how many years will the account earn interest? "))
	#collected input for principal amount, rate, years, and in-year compound frequency
	compound_total = p*(1+(r/n))**(n*t)
	compound_total = "%3.2f" % compound_total
	#calculations for output conducted
	print("")
	print("At the end of " + str(t) + " years you will have $" + str(compound_total))
	print("")
	#printed output of pertinent information

# Exercise 3-10
# PROMPT(S) (Example user input of '100', '5', '10', and '4'):
'''
Enter the number of pennies: 100
Enter the number of nickels: 5
Enter the number of dimes: 10
Enter the number of quarters: 4
'''
# OUTPUT (Less than one dollar):
'''
Sorry, the amount you entered was less than one dollar.
'''
# OUTPUT (More than one dollar):
'''
Sorry, the amount you entered was more than one dollar.
'''
# OUTPUT (Exactly one dollar):
'''
Congratulations!
The amount you entered was exactly one dollar!
You win the game!
'''
def dollar_game():
	# your code here
	p = float(input("Please enter the number of pennies: "))
	n = float(input("Please enter the number of nickels: "))
	d = float(input("Please enter the number of dimes: "))
	q = float(input("Please enter the number of quarters: "))
	#collected user inputs for number of coins
	total = ((p * 1) + (n * 5) + (d * 10) + (q * 25))
	print("")
	if total == 100:
		print('''Congratulations!
The amount you entered was exactly one dollar!
You win the game!''')
	elif total < 100:
		print("Sorry the amount you entered was less than one dollar.")
	else:
		print("Sorry the amount you entered was greater than one dollar.")
	print("")
	#calculated change total out of 100 and determined if it was larger, equal, or less than $1
# Exercise 3-12
# PROMPT(S) (Example user input of '10'):
'''
Enter the number of packages purchased: 10
'''
# OUTPUT:
'''
Discount Amount: $ 99.00
Total Amount: $ 891.00
'''
def quantity_discount():
	# your code here
	pack_no = float(input("Please enter the number of packages purchased: "))
	if pack_no >= 10 and pack_no < 20:
		discount = 0.10
	elif pack_no >= 20 and pack_no < 50:
		discount = 0.20
	elif pack_no >= 50 and pack_no < 100:
		discount = 0.30
	elif pack_no >= 100:
		discount = 0.40
	else:
		discount = 0.00
	#collected user input and determined the discount bracket accordingly
	gross_price = 99 * pack_no
	tot_discount = gross_price * discount
	gross_price -= tot_discount
	tot_discount = " %3.2f" % tot_discount
	gross_price = " %3.2f" % gross_price
	print("")
	print("Discount Amount:" + str(tot_discount))
	print("Total Amount:" + str(gross_price))
	print("")
	#calculated discount total and net price then printed output

# Exercise 3-13
# PROMPT(S) (Example user input of '10'):
'''
Enter the weight of the package: 10
'''
# OUTPUT:
'''
Shipping charge: $ 4.00
'''
def shipping_charge():
	# your code here
	pack_weight = float(input("Please enter the weight of the package in pounds: "))
	if pack_weight <= 2:
		ship_charge = 1.50
	elif pack_weight > 2 and pack_weight <= 6:
		ship_charge = 3.00
	elif pack_weight > 6 and pack_weight <= 10:
		ship_charge = 4.00
	elif pack_weight > 10:
		ship_charge = 4.75
	ship_charge *= pack_weight
	ship_charge = "%3.2f" % ship_charge
	#Collected user input of package weight and evaluated the rate bracket
	print("")
	print("Shipping Charge: $" + str(ship_charge))
	print("")

# Exercise 4-3
# PROMPT(S) (Example user input of '10', '5', and '0'):
'''
Enter amount budgeted for the month: 10
Enter an amount spent(0 to quit): 5
Enter an amount spent(0 to quit): 0
'''
# OUTPUT (Under budget):
'''
Budgeted: $ 10.00
Spent: $ 5.00
You are $ 5.00 under budget. WELL DONE!
'''
# OUTPUT (Matching budget):
'''
Budgeted: $ 10.00
Spent: $ 10.00
Spending matches budget. GOOD PLANNING!
'''
# OUTPUT (Over budget):
'''
Budgeted: $ 10.00
Spent: $ 15.00
You are $ 5.00 over budget. PLAN BETTER NEXT TIME!
'''
def budget_analysis():
	# your code here
	budget_amount = float(input("Please enter the amount budgeted for the month: "))
	amount_spent = float(input("Please enter an amount spent (0 to quit): "))
	total_spent = 0
	#initialized variables and requested input from user
	while amount_spent != 0:
		total_spent += amount_spent
		amount_spent = float(input("Please enter an amount spent (0 to quit): "))
	if total_spent < budget_amount:
		budget_difference = budget_amount - total_spent
		total_spent = "%3.2f" % total_spent
		budget_amount = "%3.2f" % budget_amount
		print("")
		print("Budgeted: $" + budget_amount)
		print("Spent: $" + total_spent)
		budget_difference = "%3.2f" % budget_difference
		print("You are $" + budget_difference + " under budget. WELL DONE!")
		print("")
	elif total_spent == budget_amount:
		total_spent = "%3.2f" % total_spent
		budget_amount = "%3.2f" % budget_amount
		print("")
		print("Budgeted: $" + budget_amount)
		print("Spent: $" + total_spent)
		print("Spending matches budget. GOOD PLANNING!")
		print("")
	else:
		budget_difference = total_spent - budget_amount
		total_spent = "%3.2f" % total_spent
		budget_amount = "%3.2f" % budget_amount
		print("")
		print("Budgeted: $" + budget_amount)
		print("Spent: $" + total_spent)
		budget_difference = "%3.2f" % budget_difference
		print ("You are $" + budget_difference + " over budget. PLAN BETTER NEXT TIME!")
		print("")
	#differentiated different scenarios and produced outcomes for each

# Exercise 4-5
# PROMPT(S) (Example user input of '1', '1', '2', '3', '4', '5', '6', '7',
# 	'8', '9', '10', '11', '12'):
'''
Enter the number of years: 1
For year  1 :
Enter the rainfall amount for the month: 1
Enter the rainfall amount for the month: 2
Enter the rainfall amount for the month: 3
Enter the rainfall amount for the month: 4
Enter the rainfall amount for the month: 5
Enter the rainfall amount for the month: 6
Enter the rainfall amount for the month: 7
Enter the rainfall amount for the month: 8
Enter the rainfall amount for the month: 9
Enter the rainfall amount for the month: 10
Enter the rainfall amount for the month: 11
Enter the rainfall amount for the month: 12
'''
# OUTPUT:
'''
For  12 months
Total rainfall:  78.00 inches
Average monthly rainfall:  6.50 inches
'''
def average_rainfall():
	# your code here
	yrs = int(input("Please enter the number of years: "))
	mon = 0
	rain_amount = 0
	#initialized and gathered input for variables
	for i in range(1, yrs + 1):
		print("For Year " + str(i) + ": ")
		for j in range(1, 13):
			rain_amount += float(input("Please enter the rainfall amount for month " + str(j) + ": "))
			mon += 1
	#ran nested loops to gather data
	print("")
	print("For " + str(mon) + " Months:")
	avg_rainfall = rain_amount / mon
	avg_rainfall = "%3.2f" % avg_rainfall
	rain_amount = "%3.2f" % rain_amount
	print("Total rainfall: " + rain_amount)
	print("Average Monthly Rainfall: " + avg_rainfall)
	print("")
	#printed output in accordance with inputs

# Exercise 4-12
# PROMPT(S) (Example user input of '10'):
'''
Enter a nonnegative integer: 10
'''
# OUTPUT:
'''
The factoral of 10 is 3628800
'''
def factorial():
	# your code here
	nni = int(input("Please enter a nonnegative integer: "))
	fac_comp = 1
	nni2 = nni
	while nni2 != 0:
		fac_comp *= nni2
		nni2 -= 1
	print("")
	print("The factorial of " + str(nni) + " is " + str(fac_comp) + ".")
	print("")

# Exercise 8-4
# PROMPT(S) (Example user input of 'python'):
'''
Enter the string to be converted to Morse code: python
'''
# OUTPUT:
'''
--.-,--..,..-,..,.--.,---,
'''
def morse_code():
	# your code here
	morse_dict = {" " : " ", "," : "--..--", "." : ".-.-.-", "?" : "..--..", "0" : "-----", "1" : ".----", 
	"2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..",
	"9" : "----.", "A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", "F" : "..-.", "G" : "--.",
	"H" : "....", "I" : "..", "J" : ".---", "K" : "-.-", "L" : ".-..", "M" : "--", "N" : "-.", "O" : "---",
	"P" : ".--.", "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-", "U" : "..-", "V" : "...-", "W" : ".--",
	"X" : "-..-", "Y" : "-.-", "Z" : "--.."}
	raw_string = input("Please enter the string to be convereted to Morse Code: ")
	upper_string = raw_string.upper()
	list_string = list(upper_string)
	print("")
	for i in range(0, len(upper_string)):
		print(morse_dict[list_string[i]] + ',', end = '')
	print("")
	
# *** DO NOT EDIT BELOW THIS POINT ***
# This part of the file is for testing purposes.
# Your code WILL FAIL the test cases if this is edited.
def main():
	# run each exercise
	sales_tax()
	compound_interest()
	dollar_game()
	quantity_discount()
	shipping_charge()
	budget_analysis()
	average_rainfall()
	factorial()
	morse_code()

if __name__=="__main__":
	main()
