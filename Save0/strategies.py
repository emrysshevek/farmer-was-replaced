def handle_tile(x, y):
	#quadrants(x, y)
	basics(x, y)
	water()

def handle_grass(x, y):
	base_harvest()
	plant_grass()
	
def handle_wood(x, y):
	base_harvest()
	plant_wood()
	
def handle_carrots(x, y):
	base_harvest()
	plant_carrots()
	 
def handle_pumpkins(x, y):
	base_harvest()
	plant_pumpkins()
	
def handle_sunflowers(x, y):
	if get_entity_type() != Entities.Sunflower:
		base_harvest()
		plant_sunflower()
		if (x, y) == globals["sections"]["sunflower"]["coordinates"][1]:
			globals["sunflower"]["state"] = "harvesting"
	else:
		count = measure()
		if count > globals["sunflower"]["max_val"]:
			globals["sunflower"]["max_val"] = count
			globals["sunflower"]["coordinates"] = (x, y)
			
		if (x, y) == globals["sections"]["sunflower"]["coordinates"][1]:
			(target_x, target_y) = globals["sunflower"]["coordinates"]
			if target_x >= 0:
				move_to(target_x, target_y)
				harvest()
				plant_sunflower()
				move_to(x, y)
			globals["sunflower"]["coordinates"] = (-1, -1)
			globals["sunflower"]["max_val"] = -1
			start_x, start_y = globals["sections"]["sunflower"]["coordinates"][0]
			globals["sunflower"]["state"] = "planting"

def handle_cactus(start_x, start_y):
	if get_entity_type() == Entities.Cactus:
		sorted = False
		size = measure()
		x, y = (start_x, start_y)
		while not sorted:
			sorted = True
			for dir in directions:
				move(dir)
				new_size = measure()
				new_x, new_y = (get_pos_x(), get_pos_y())
				if get_entity_type() == Entities.Cactus:
					if new_size < size and (new_x > x or new_y > y):
						swap(reverse(dir))
						sorted = False
						x, y = (new_x, new_y)
						break
				else:
					move(reverse(dir))
		move_to(start_x, start_y)
		if (start_x, start_y) == globals["sections"]["cactus"]["coordinates"][1]:
			base_harvest()
	else:
		base_harvest()
		plant_cactus()
	
	
def basics(x, y):
	handle_grass(x, y)
	

def quadrants(x, y):
	quadrant_size = get_world_size() / 2
	if x < quadrant_size and y < quadrant_size:
		handle_pumpkins(x, y)
	elif x < quadrant_size and y >= quadrant_size:
		handle_carrots(x, y)
	elif x >= quadrant_size and y < quadrant_size:
		handle_wood(x, y)
	elif x >= quadrant_size and y >= quadrant_size:
		handle_grass(x, y)
		