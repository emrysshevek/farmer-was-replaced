def random_elem(list):
	return list[random() * len(list) // 1]
	
def under_threshold(threshold):
	res = True
	for item in threshold:
		if num_items(item) >= threshold[item]:
			res = False
	return res

def under_time(time):
	return get_time() < time
	
def benchmark(func, arg):
	time = get_time()
	ops = get_op_count()
	func(arg)
	quick_print("Time:", get_time() - time, " ops:", get_op_count() - ops)
	
def get_section(x, y):
	for section in globals["sections"]:
		lbound, hbound = globals["sections"][section]["coordinates"]
		if x >= lbound[0] and x <= hbound[0] and y >= lbound[1] and y <= hbound[1]:
			return section
	print("Invalid section coordinates")
	return None
	
def turn_right(direction):
	return {North: East, East: South, South: West, West: North}[direction]
	
def turn_left(direction):
	return {North: West, West: South, South: East, East: North}[direction]
	
def reverse(direction):
	return {North: South, South: North, East: West, West: East}[direction]

def get_position():
	return (get_pos_x(), get_pos_y())
	
def directions_to(target, position):
	xdiff = target[0] - position[0]
	ydiff = target[1] - position[1]
	
	x_dir = None
	y_dir = None
	
	if xdiff > 0:
		x_dir = East
	elif xdiff < 0:
		x_dir = West
		
	if ydiff > 0:
		y_dir = North
	elif ydiff < 0:
		y_dir = South
		
	if abs(xdiff) <= abs(ydiff):
		return (x_dir, y_dir)
	else:
		return (y_dir, x_dir)

def direction_to(target, position):
	xdiff = target[0] - position[0]
	ydiff = target[1] - position[1]
	if xdiff > 0 and ydiff == 0:
		return East
	elif xdiff < 0 and ydiff == 0:
		return West
	elif xdiff == 0 and ydiff > 0:
		return North
	elif xdiff == 0 and ydiff < 0:
		return South
	else:
		return None