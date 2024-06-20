def PolycultureHandler():
	
	def poly_iterate(self):
		if not self["is_ready"]:
			self["init"]()
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				position = (i, j)
				move_to(position)
				self["harvest"](position)
				self["plant"](position)
				self["record"](position)
	#enddef
	
	def poly_plant(self, position):
		entity = random_elem(self["entities"])
		plant_entity(entity)
	#enddef
	
	def poly_harvest(self, position):
		companion = get_companion()
		if companion != None:
			entity, e_x, e_y = companion
			if self["values"][(e_x, e_y)] != entity:
				move_to((e_x, e_y))
				if get_entity_type() != entity:
					harvest()
				plant_entity(entity)
				move_to(position)
		harvest()
	#enddef
	
	def poly_record(self, position):
		self["values"][position] = get_entity_type()
	#enddef
		
	def poly_kill(self):
		self["values"] = {}
		self["is_ready"] = False
	#enddef
		
	return {
		"class_name": "PolycultureHandler",
		"inherits": [BaseHandler],
		"properties": [
			("entities", [Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrots]),
			("values", {}),
		],
		"methods": [
			("iterate", poly_iterate, 0),
			("plant", poly_plant, 1),
			("harvest", poly_harvest, 1),
			("record", poly_record, 1),
			("kill", poly_kill, 0),
		]
	}
#enddef

harvest()
handler = new(PolycultureHandler())
#handler["log"](0)
handler["iterate"]()