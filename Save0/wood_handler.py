def WoodHandler():
	
	def wood_plant(self, position):
		x, y = position
		if x % 2 == y % 2:
			plant_entity(Entities.Bush)
		else:
			plant_entity(Entities.Tree)

	return {
		"class_name": "HayHandler",
		"inherits": [PolycultureHandler],
		"methods": [
			("plant", wood_plant, 1),
		]
	}
#enddef

harvest()
handler = new(WoodHandler())
handler["iterate"]()