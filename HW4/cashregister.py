class CashRegister():

	def __init__(self):
		self.Item_List = []

	def purchase_item(self, item):
		self.Item_List.append(item)
		return self.Item_List

	def get_total(self):
		total = 0
		for item in self.Item_List:
			total += item.Price
		return total

	def show_items(self):
		for item in self.Item_List:
			print("")
			print("Description: "  + item.Description)
			print("Units in inventory: " + str(item.UnitsinInventory))
			print("Price: $" + "%3.2f" % item.Price)
			print("")

	def clear(self):
		self.Item_List = []
