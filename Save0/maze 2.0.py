def update_graph(a, b, dist, conn):
	if b in dist[a] and dist[a][b] == 1 and a in dist[b] and dist[b][a] == 1:
		return
	
	# update matrices
	dist[a][b] = 1
	dist[b][a] = 1
	conn[a][b] = b
	conn[b][a] = a
	
	# if distance to a tile is shorter going through the new tile,
	# update matrices again
	for c in dist[a]:
		if c not in dist[b] or dist[b][c] > 1 + dist[a][c]:
			dist[b][c] = 1 + dist[a][c]
			dist[c][b] = 1 + dist[a][c]
			conn[b][c] = a
			conn[c][b] = conn[c][a]
		if dist[a][c] > 1 + dist[b][c]:
			dist[a][c] = 1 + dist[b][c]
			dist[c][a] = 1 + dist[c][b]
			conn[a][c] = b
			conn[c][a] = conn[c][b]
			
	# doesn't seem to be used very often. might add back in later
	for c in dist[b]:
		if c not in dist[a] or dist[a][c] > 1 + dist[b][c]:
			dist[a][c] = 1 + dist[b][c]
			conn[a][c] = b
			conn[c][a] = conn[c][b]
		if dist[b][c] > 1 + dist[a][c]:
			dist[b][c] = 1 + dist[a][c]
			conn[b][c] = a
			conn[c][b] = conn[c][a]

def update_epsilon(epsilon, stats):
	iter_val = min(stats["iters"] / stats["max_iters"], 1)
	step_val = min(stats["steps"] / stats["max_steps"], 1)
	return iter_val + ((1 - iter_val) * step_val)
	
def choose_move_and_update_graph(target, epsilon, dist, conn):
	position = get_position()
	if random() < epsilon:
		new_position = choose_optimal(target, position, dist, conn)
		if new_position != None:
			update_graph(position, new_position, dist, conn)
	else:
		new_position = choose_explore(target, position, dist, conn)
		update_graph(position, new_position, dist, conn)
		
def choose_explore(target, position, dist, conn):
	directions = directions_to(target, position)
	if directions[0] == None:
		return position
	for dir in directions_to(target, position):
		if move(dir):
			return get_position()
	return choose_random(target, position, dist, conn) 

def choose_random(target, position, dist, conn):
	dir = random_elem(globals["directions"])
	while not move(dir):
		dir = random_elem(globals["directions"])
	return (get_pos_x(), get_pos_y())

def choose_optimal(target, position, dist, conn):
	if target in conn[position]:
		quick_print(conn[position][target])
		direction = direction_to(conn[position][target], position)
		if direction == None:
			return choose_random(target, position, dist, conn)
		elif move(direction):
			return None
		else:
			quick_print("ERROR: optimal choice failed")
	return choose_random(target, position, dist, conn)

def navigate_to(target, conn):
	quick_print("navigating to ", target)
	position = get_position()
	while position != target:
		quick_print("current position ", position)
		next_pos = conn[position][target]
		dir = direction_to(next_pos, position)
		move(dir)
		position = next_pos

def build_graph(dist, conn):
	visited = {}
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			visited[(i,j)] = False

	queue = [get_position()]
	
	while len(queue) > 0:
		# remove next tile from queue and move to that location
		position = queue.pop()
		if visited[position]:
			continue
		quick_print("checking tile", position)
		navigate_to(position, conn)
		
		# update graph in all directions
		for dir in globals["directions"]:
			if move(dir):
				neighbor_pos = get_position()
				update_graph(position, neighbor_pos, dist, conn)
				# add neighbor to queue and return to original tile
				if not visited[neighbor_pos]:
					queue.append(neighbor_pos)
				move(reverse(dir))
		visited[position] = True

def blind_solve(dist, conn):
	direction = North
	x, y = (get_pos_x(), get_pos_y())
	while True:
		if get_entity_type() == Entities.Treasure:
			return (x, y)
		
		next_dir = turn_right(direction)
		
		for i in range(len(globals["directions"])):
			if move(next_dir):
				direction = next_dir
				next_x, next_y = (get_pos_x(), get_pos_y())
				update_graph((x, y), (next_x, next_y), dist, conn)
				(x, y) = (next_x, next_y)
				break
			else:
				next_dir = turn_left(next_dir)

def solve():
	dist = {}
	conn = {}
	
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			dist[(i, j)] = {(i,j): 0}
			conn[(i, j)] = {(i, j): (i, j)}
	build_graph(dist, conn)
	target = blind_solve(dist, conn)
	epsilon = 0.85
	stats = {"iters": 0, "steps": 0, "max_iters": 300, "max_steps": get_world_size() ** 2}
	total_steps = 0
	while stats["iters"] < 300 and num_items(Items.Fertilizer) > 0:
		if stats["steps"] > get_world_size() ** 2:
			target = blind_solve(dist, conn)
			stats["iters"] += 1
			stats["steps"] = 0
		
		choose_move_and_update_graph(target, epsilon, dist, conn)
		
		if get_entity_type() == Entities.Treasure:
			target = measure()
			while get_entity_type() == Entities.Treasure:
				fertilize()
			stats["iters"] += 1
			stats["steps"] = 0
		else:
			stats["steps"] += 1
		
		total_steps += 1
		#if total_steps % 5 == 0:	
			#epsilon = update_epsilon(epsilon, stats)
	# end while
	harvest()
	
def spawn_maze():
	harvest()
	base_plant(Entities.Bush, Grounds.Soil)
	while get_entity_type() != Entities.Hedge:
		fertilize()

globals = {}
init_globals(globals)
spawn_maze()
solve()
			
