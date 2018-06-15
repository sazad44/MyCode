def main():
	import retailitem
	jacket = retailitem.RetailItem("Jacket", 12, 59.95)
	jeans = retailitem.RetailItem("Designer Jeans", 40, 34.95)
	shirt = retailitem.RetailItem("Shirt", 20, 24.95)
	jacket.Price = "%3.2f" % jacket.Price
	print("")
	print("Retail Item 1:")
	print("Description: " + jacket.Description)
	print("Units in inventory: " + str(jacket.UnitsinInventory))
	print("Price: $" + jacket.Price)
	jeans.Price = "%3.2f" % jeans.Price
	print("")
	print("Retail Item 2:")
	print("Description: " + jeans.Description)
	print("Units in inventory: " + str(jeans.UnitsinInventory))
	print("Price: $" + jeans.Price)
	shirt.Price = "%3.2f" % shirt.Price
	print("")
	print("Retail Item 3:")
	print("Description: " + shirt.Description)
	print("Units in inventory: " + str(shirt.UnitsinInventory))
	print("Price: $" + shirt.Price)
	print("")

if __name__ == "__main__":
	main()