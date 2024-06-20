def BaseHandler():

	def init(self):
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				position = (i,j)
				move_to(position)
				harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				self["plant"](position)
				self["record"](position)
		self["is_ready"] = True
	#enddef
	
	def iterate(self):
		if not self["is_ready"]:
			self["init"]()
	#enddef

	def plant_(self, position):
		self["error"]("Plant not implemented")
	#enddef
	
	def harvest_(self, position):
		self["error"]("Harvest not implemented")
	#enddef
	
	def record(self, position):
		pass
	#enddef
	
	return {
		"class_name": "BaseHandler",
		"methods": [
			("init", init, 0),
			("iterate", iterate, 0),
			("plant", plant_, 1),
			("harvest", harvest_, 1),
			("record", record, 1),
		]
	}

harvest()
handler = new(BaseHandler())
handler["log"](0)
handler["init"]()