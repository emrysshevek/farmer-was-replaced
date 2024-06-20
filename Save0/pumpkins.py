
def plant_pumpkins():
	bounds = globals["sections"]["pumpkin"]["coordinates"]
	empty_plots = []
	
	for i in range(bounds[0][0], bounds[1][0] + 1):
			for j in range(bounds[0][1], bounds[1][1] + 1):
				empty_plots.append((i, j))
				
	while len(empty_plots) > 0:
		for i in range(len(empty_plots)-1, -1, -1):
			x, y = empty_plots[i]
			move_to(x, y)
			if get_entity_type() != Entities.Pumpkin:
				harvest()
				plant_pumpkin()
				fertilize()
			elif can_harvest():
				empty_plots.pop(i)

def harvest_pumpkins():
	plant_pumpkins()
	harvest()

globals = {}
init_globals(globals)
prioritize("pumpkin")
harvest()
plant_pumpkins()
			