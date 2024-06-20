def advance():
	move(North)
	if get_pos_y() == 0:
		move(East)
		
def move_to(x, y):
	return move_to((x,y))

def move_to(position):
	x, y = position
	last_move = None
	curr_x, curr_y = (get_pos_x(), get_pos_y())
	size = get_world_size()
	
	diff = x - curr_x
	wrap_left = (x - size) - curr_x
	wrap_right = (x + size) - curr_x
	wrap_diff = wrap_left
	if abs(wrap_right) < abs(wrap_diff):
		wrap_diff = wrap_right
	if abs(wrap_diff) < abs(diff):
		diff = wrap_diff
	dir = East
	if diff < 0:
		dir = West
	for i in range(abs(diff)):
		move(dir)
		last_move = dir
		
	diff = y - curr_y
	wrap_left = (y - size) - curr_y
	wrap_right = (y + size) - curr_y
	wrap_diff = wrap_left
	if abs(wrap_right) < abs(wrap_diff):
		wrap_diff = wrap_right
	if abs(wrap_diff) < abs(diff):
		diff = wrap_diff
	dir = North
	if diff < 0:
		dir = South	
	for i in range(abs(diff)):
		move(dir)
		last_move = dir
	return last_move