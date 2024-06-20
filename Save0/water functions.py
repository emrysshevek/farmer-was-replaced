def water():
	while get_water() < 1:
		use_item(Items.Water_Tank)
	restock(Items.Empty_Tank, 1000, 2000)