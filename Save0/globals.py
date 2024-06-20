def init_globals(globals):
	globals["directions"] = [North, East, South, West]
	
	radius = (get_world_size() - 1) // 2
	globals["sections"] = {
		"poly": {
			"entities": [Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrots],
			"coordinates": [(0, 0), (radius, radius)]
		},
		"pumpkin": {
			"entities": [Entities.Pumpkin],
			"coordinates": [(radius , 0), (get_world_size() - 1, radius)]
		},
		"sunflower": {
			"entities": [Entities.Sunflower],
			"coordinates": [(0, radius + 1), (radius, get_world_size() - 1)]
		},
		"cactus": {
			"entities": [Entities.Cactus],
			"coordinates": [(radius + 1, radius + 1), (get_world_size() - 1, get_world_size() - 1)]
		}
	}
	
	globals["sunflower"] = {
		"values": list(),
		"state": "planting"
	}
	
	globals["cactus"] = {
		"values": list()
	}
	
	globals["spawn_maze"] = False
		