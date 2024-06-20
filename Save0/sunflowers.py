def cmp_flowers(a, b):
	return a[1] - b[1]

def init_sunflowers():
	heap = list()
	
	bounds = globals["sections"]["sunflower"]["coordinates"]
	for i in range(bounds[0][0], bounds[1][0] + 1):
		for j in range(bounds[0][1], bounds[1][1] + 1):
			move_to(i, j)
			harvest()
			plant_sunflower()
			
	for i in range(bounds[0][0], bounds[1][0] + 1):
		for j in range(bounds[0][1], bounds[1][1] + 1):
			move_to(i, j)
			position = get_position()
			if get_entity_type() == Entities.Sunflower:
				heap_push(heap, (position, measure()), cmp_flowers)
			else:
				plant_sunflower()
				while get_entity_type() != Entities.Sunflower:
					pass
				heap_push(heap, (position, measure()), cmp_flowers)
				
	globals["sunflower"]["values"] = heap

def harvest_sunflower():
	heap = globals["sunflower"]["values"]
	best = heap[0][0]
	move_to(best[0], best[1])
	while not can_harvest():
		pass
	harvest()
	plant_sunflower()
	fertilize()
	while get_entity_type() != Entities.Sunflower:
		pass
	heap_replace(heap, (best, measure()), cmp_flowers)