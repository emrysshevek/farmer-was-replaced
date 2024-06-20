def PumpkinHandler():
	
	def iterate(self):
		pass
	#enddef
	
	def record(self, position):
		self["values"].append(position)
	#enddef
		
	def kill(self):
		self["values"] = {}
		self["super"]["kill"]()
	#enddef
		
	return {
		"class_name": "PolycultureHandler",
		"inherits": [BaseHandler],
		"properties": [
			("values", []),
		],
		"methods": [
			("plant", plant_, 1),
			("harvest", harvest_, 1),
			("record", record, 1),
			("kill", kill, 0),
		]
	}
#enddef

harvest()
handler = new(PumpkinHandler())
handler["iterate"]()