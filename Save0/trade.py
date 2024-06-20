def restock(item, low, high):
	count = num_items(item)
	if count < low:
		count = high - count
		cost = get_cost(item)
		for elem in cost:
			count = min(count, num_items(elem) // cost[elem])
		trade(item, count)
			