def cmp_tuple(a, b):
	return a[1] - b[1]

def left(idx):
	return idx * 2 + 1

def right(idx):
	return idx * 2 + 2

def parent(idx):
	return (idx-1)//2
	
def bubble_up(heap, idx, cmp):
	elem = heap[idx]	
	while idx > 0:
		p_idx = parent(idx)
		if cmp(elem, heap[p_idx]) > 0:
			heap[idx] = heap[p_idx]
			heap[p_idx] = elem
			idx = p_idx
		else:
			break
	return heap
	
def bubble_down(heap, idx, cmp):
	elem = heap[0]
	length = len(heap) - 1
	
	while idx < length:
		l_idx = left(idx)
		r_idx = right(idx)
		largest = idx
		
		if l_idx <= length and cmp(heap[l_idx], elem) > 0:
			largest = l_idx
		if r_idx <= length and cmp(heap[r_idx], heap[largest]) > 0:
			largest = r_idx
		
		if largest != idx:
			heap[idx] = heap[largest]
			heap[largest] = elem
			idx = largest
		else:
			break
	
	return heap
	
def heap_push(heap, elem, cmp):
	heap.append(elem)
	return bubble_up(heap, len(heap) - 1, cmp)	
	
def heap_pop(heap, cmp):
	if len(heap) == 0:
		return None
	elif len(heap) <= 2:
		return heap.pop(0)
		
	result = heap[0]
	heap[0] = heap.pop()
	bubble_down(heap, 0, cmp)
	
	return result
	
def heap_push_pop(heap, elem, cmp):
	if cmp(elem, heap[0]) > 0:
		return elem
	else:
		result = heap[0]
		heap[0] = elem
		bubble_down(heap, 0, cmp)
		return result

def heap_replace(heap, elem, cmp):
	result = heap[0]
	heap[0] = elem
	bubble_down(heap, 0, cmp)
	return result