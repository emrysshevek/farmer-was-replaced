def base_plant(entity, soil):
	if get_ground_type() != soil:
		till()
	if get_entity_type != entity:
		plant(entity)
	if get_water() <= .75:
		restock(Items.Empty_Tank, 500, 1000)
		water()

def plant_entity(entity):
	if entity == Entities.Grass:
		plant_grass()
	elif entity == Entities.Bush:
		plant_bush()
	elif entity == Entities.Tree:
		plant_tree()
	elif entity == Entities.Carrots:
		plant_carrots()
	elif entity == Entities.Sunflower:
		plant_sunflower()

def fertilize():
	restock(Items.Fertilizer, 500, 1000)
	use_item(Items.Fertilizer)

def plant_grass():
	base_plant(Entities.Grass, Grounds.Soil)
	
def plant_bush():
	base_plant(Entities.Bush, Grounds.Soil)
	
def plant_tree():
	base_plant(Entities.Tree, Grounds.Soil)

def plant_wood():
	if get_pos_y() % 2 == get_pos_x() % 2:
		plant_bush()
	else:
		base_plant(Entities.Tree, Grounds.Soil)
	base_plant(Entities.Bush, Grounds.Soil)

def plant_carrots():
	restock(Items.Carrot_Seed, 100, 200)
	base_plant(Entities.Carrots, Grounds.Soil)
	
def plant_sunflower():
	restock(Items.Sunflower_Seed, 100, 200)
	base_plant(Entities.Sunflower, Grounds.Soil)

def plant_pumpkin():
	restock(Items.Pumpkin_Seed, 100, 200)
	base_plant(Entities.Pumpkin, Grounds.Soil)
	
def plant_cactus():
	restock(Items.Cactus_Seed, 100, 200)
	base_plant(Entities.Cactus, Grounds.Soil)