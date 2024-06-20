def HayHandler():
	
	def plant_(self, position):
		plant_entity(Entities.Grass)
		
	return {
		"class_name": "HayHandler",
		"inherits": [PolycultureHandler],
		"methods": [
			("plant", plant_, 1),
		]
	}
#enddef

harvest()
handler = new(HayHandler())
handler["iterate"]()