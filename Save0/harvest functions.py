def base_harvest():
	if can_harvest():
		harvest()

def harvest_entity(entity, x, y):
	if entity == Entities.Bush:
		harvest_bush(x, y)
	elif entity in globals["sections"]["poly"]["entities"]:
		harvest_poly(x, y)
	else:
		base_harvest()

def harvest_poly(x, y):
	if can_harvest():
		entity, target_x, target_y = get_companion()
		if get_section(target_x, target_y) == "poly":
			move_to(target_x, target_y)
			plant_entity(entity)
			move_to(x, y)
		harvest()

def harvest_bush(x, y):
	if can_harvest():
		if globals["spawn_maze"]:
			fertilize()
			if get_entity_type() == Entities.Hedge:
				solve()
		harvest_poly(x, y)

	