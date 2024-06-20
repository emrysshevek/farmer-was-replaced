def get_max_dir(position):
	max_dir = None
	max_size = measure()
	lbound = globals["sections"]["cactus"]["coordinates"][0]
	if position[0] > lbound[0]: 
		move(West)
		if measure() > max_size:
			max_dir = West
			max_size = measure()
		move(East)
	
	if position[1] > lbound[1]:
		move(South)
		if measure() > max_size:
			max_dir = South
		move(North)
	
	return max_dir

def reposition_cactus():
	size = measure()
	position = get_position()
	while True:
		dir = get_max_dir(position)
		if dir == None:
			break
		else:
			swap(dir)
			move(dir)
			position = get_position()	 
		
def init_cactuses():
	bounds = globals["sections"]["cactus"]["coordinates"]
	for i in range(bounds[0][0], bounds[1][0] + 1):
			for j in range(bounds[0][1], bounds[1][1] + 1):
				move_to(i, j)
				if get_entity_type() != Entities.Cactus:
					harvest()
					plant_cactus()
					fertilize()
				reposition_cactus()
	harvest()

					
def harvest_cactuses():
	bounds = globals["sections"]["cactus"]["coordinates"]
	heap = globals["cactus"]["values"]
	coords = globals["cactus"]["coords"]
	for i in range(bounds[0][0], bounds[1][0] + 1):
			for j in range(bounds[0][1], bounds[1][1] + 1):
				cactus = heap_pop(heap, cmp_cactus)
				reposition_cactus((i, j), cactus, c)
	harvest()
				

globals = {}
init_globals(globals)
prioritize("cactus")
clear()
init_cactuses()