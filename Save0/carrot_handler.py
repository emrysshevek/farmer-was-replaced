def CarrotHandler():
	
	def plant_(self, position):
		plant_entity(Entities.Carrots)

	return {
		"class_name": "CarrotHandler",
		"inherits": [PolycultureHandler],
		"methods": [
			("plant", plant_, 1),
		]
	}
#enddef

harvest()
handler = new(CarrotHandler())
handler["iterate"]()