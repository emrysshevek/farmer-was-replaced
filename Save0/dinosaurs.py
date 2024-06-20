def plant_dinosaurs():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			move_to(i,j)
			harvest()
			trade(Items.Egg)
			use_item(Items.Egg)

def swap_to_corner(position, dir):
	while position[0] > 0 and position[0] < get_world_size() - 1:
		swap(xdir)
		move(xdir)
		position = get_position()
	while position[1] > 0 and position[1] < get_world_size() - 1:
		swap(ydir)
		move(ydir)
		position = get_position()
	
def harvest_dinosaurs():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			move_to(i, j)
			position = get_position()
			val = measure()
			if val == 0:
				swap_to_corner(position, North)
			elif val == 1:
				swap_to_corner(position, East)
			elif val == 2:
				swap_to_corner(position, South)
			else:
				swap_to_corner(position, West)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			move_to(i,j)
			harvest()
clear()
plant_dinosaurs()
harvest_dinosaurs()