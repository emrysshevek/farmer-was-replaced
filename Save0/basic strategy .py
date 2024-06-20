
		
def handle_group(x, y):
	harvest_entity(get_entity_type(), x, y)
	entity = random_elem(globals["sections"]["poly"]["entities"])
	plant_entity(entity)

def prioritize(priority):
	for section in globals["sections"]:
		if section == priority:
			globals["sections"][section]["coordinates"] = ((0,0), (get_world_size()-1, get_world_size()-1))
		else:
			globals["sections"][section]["coordinates"] = ((-1, -1), (-1, -1))
	
def basic_strategy():
	x, y = (get_pos_x(), get_pos_y())
	
	section = get_section(x, y)
	if section == "poly":
		handle_group(x, y)
	elif section == "pumpkin":
		handle_pumpkins(x, y)
	elif section == "sunflower":
		handle_sunflowers(x, y)
	elif section == "cactus":
		handle_cactus(x, y)
	
	advance()
	