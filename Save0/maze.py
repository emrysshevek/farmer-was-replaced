def pos_mod(a, b):
	return ((a % b) + b) % b

def turn_right(dir_idx):
	return (dir_idx + 1) % 4

def turn_left(dir_idx):
	return ((dir_idx - 1 % 4) + 4) % 4
	
def reverse(dir_idx):
	return ((dir_idx + 2 % 4) + 4) % 4
	
def flatten(x, y):
	return y * get_world_size() + x

def unflatten(idx):
	if idx == 0:
		return (0, 0)
	return (idx % get_world_size(), idx // get_world_size())



def build_graph_old(distances, connections):
	directions = [North, East, South, West]
	# init matricies
	visited = []
	for i in range(get_world_size() ** 2):
		distances.append([])
		connections.append([])
		visited.append(False)
		for j in range(get_world_size() ** 2):
			distances[i].append(1000000)
			connections[i].append(None)
		distances[i][i] = 0
		connections[i][i] = i

	queue = [(get_pos_x(), get_pos_y())]
	
	while len(queue) > 0:
		# remove next tile from queue and move to that location
		x, y = queue.pop()
		curr_idx = flatten(x, y)
		if visited[curr_idx]:
			continue
		quick_print("checking tile (", x, ", ", y, "). idx ", curr_idx)
		navigate_to(x, y, connections)
		
		# update graph in all directions
		for dir_idx in range(len(directions)):
			if move(directions[dir_idx]):
				neighbor_x = get_pos_x()
				neighbor_y = get_pos_y()
				neighbor_idx = flatten(get_pos_x(), get_pos_y())
				update_graph(curr_idx, neighbor_idx, dir_idx, distances, connections)
				# add neighbor to queue and return to original tile
				if not visited[neighbor_idx]:
					queue.append((neighbor_x, neighbor_y))
				move(directions[reverse(dir_idx)])
		quick_print(distances)
		visited[curr_idx] = True



def solve_maze():
	#if num_items(Items.Fertilizer) < 50:
	blind_solve()
	harvest()
	return
		
	directions = [North, East, South, West]
	distances = []
	connections = []
	
	build_graph(distances, connections)
	
	blind_solve()
	respawns = 299
	while num_items(Items.Fertilizer) > 0 and respawns > 0:
		x, y = measure()
		fertilize()
		if get_entity_type() != Entities.Treasure:
			respawns -= 1
			navigate_to(x, y, connections)
	
	harvest()

	
		
		