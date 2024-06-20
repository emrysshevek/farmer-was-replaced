def harvest_wood():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			move_to(i,j)
			c, x, y = get_companion()
			if c != None:
				move_to(x, y)
				harvest()
				plant_entity(c)
				move_to(i,j)
			harvest()
			
			plant_tree()

def maximize_wood(threshold):
	while under_threshold(threshold):
		harvest_wood()
		
benchmark(maximize_wood, {Items.Wood: num_items(Items.Wood) + 5000})