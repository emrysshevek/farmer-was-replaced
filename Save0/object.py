def Object():
	
	def init(self):
		quick_print("Object init")
	#enddef
		
	def iterate(self):
		self["error"]("Iterate Not Implemented")
	#enddef
	
	def run(self, threshold, time_limit):
		while under_threshold(threshold) and under_time(get_time() + time_limit):
			self["iterate"]()
	#enddef
	
	def kill(self):
		self["is_ready"] = False
	#enddef
		
	def error(self, message):
		print("[", self["class_name"], "] ERROR:", message)
		return self["__this_key_does_not_exist__"]
	#enddef
	
	def log(self, level):
		space = ""
		for i in range(level):
			space += "  "
			
		quick_print(space, "Logging", self["class_name"])
		for elem in self:
			quick_print(space + "  ", elem, ":", self[elem])
	#enddef
	
	return {
		"class_name": "Object",
		"properties": [
			("is_ready", False),
			("is_running", False)
		],
		"methods": [
			("init", init, 0),
			("iterate", iterate, 0),
			("run", run, 2),
			("kill", kill, 0),
			("error", error, 1),
			("log", log, 1),
		]
	}
#enddef