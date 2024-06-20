def clone(obj):
	new_obj = {}
	for elem in obj:
		new_obj[elem] = obj
	return new_obj
#enddef

def new(child_class):
	new_object = {}

	def add_properties(class, obj):
		if "properties" in class:
			for prop in class["properties"]:
				name, val = prop
				obj[name] = val
		return obj
	#enddef
		
	def add_method(method, obj, self): 
		name, fnc, nargs = method

		wrapper = None
		if nargs == 0:
			def obj_wrapper0():
				return fnc(self)
			wrapper = obj_wrapper0
		elif nargs == 1:
			def obj_wrapper1(a):
				return fnc(self, a)
			wrapper = obj_wrapper1
		elif nargs == 2:
			def obj_wrapper2(a, b):
				return fnc(self, a, b)
			wrapper = obj_wrapper2
		elif nargs == 3:
			def obj_wrapper3(a, b, c):
				return fnc(self, a, b, c)
			wrapper = obj_wrapper3
		elif nargs == 4:
			def obj_wrapper4(a, b, c, d):
				return fnc(self, a, b, c, d)
			wrapper = obj_wrapper4
		elif nargs == 5:
			def obj_wrapper5(a, b, c, d, e):
				return fnc(self, a, b, c, d, e)
			wrapper = obj_wrapper5
					
		obj[name] = wrapper
		return obj
	#enddef
	
	def add_supers(class, obj):
		if class["class_name"] != "Object":
			if "inherits" not in class:
				class["inherits"] = [Object]
				
			while len(class["inherits"]) > 0:
				parent_class = class["inherits"].pop()()
				inherit = inflate_obj(parent_class, {}, obj)
				for elem in inherit:
					obj[elem] = inherit[elem]
					
		return obj
	#enddef
	
	def inflate_obj(class, obj, self):		
		add_supers(class, obj)
		add_properties(class, obj)
		if "methods" in class:
			for method in class["methods"]:
				add_method(method, obj, self)
		obj["class_name"] = class["class_name"]
		return obj
	#enddef

	new_object = inflate_obj(child_class, new_object, new_object)
	return new_object
#enddef
	